from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
URL = 'http://www.uitestingplayground.com/'
WAIT_TIME = 10

# Common Functions
def navigate_to_page():
    driver.get(URL)

def wait_for_element(selector):
    return WebDriverWait(driver, WAIT_TIME).until(
        EC.presence_of_element_located(selector)
    )

# Test Functions
def visibility_test():
    try:
        navigate_to_page()

        visibility_link = wait_for_element((By.LINK_TEXT, 'Visibility'))
        visibility_link.click()

        hide_button = wait_for_element((By.ID, 'hideButton'))
        hide_button.click()

        buttons = driver.find_elements(By.XPATH, '//button[@class="btn-primary"]')
        hidden = all(not button.is_displayed() for button in buttons)

        if hidden:
            print("Btns are hidden.")
        else:
            print("The btn are visible")

    finally:
        driver.quit()

def progress_bar_test():
    try:
        navigate_to_page()

        progress_bar_link = wait_for_element((By.LINK_TEXT, 'Progress Bar'))
        progress_bar_link.click()

        start_button = wait_for_element((By.ID, 'startButton'))
        start_button.click()

        stop_button = wait_for_element((By.ID, 'stopButton'))
        stop_button.click()

        duration_element = wait_for_element((By.ID, 'result'))
        duration = duration_element.text

        print(f"Duration: {duration}")

    finally:
        driver.quit()

def input_text_test():
    try:
        navigate_to_page()

        text_input_link = wait_for_element((By.LINK_TEXT, 'Text Input'))
        text_input_link.click()

        input_field = wait_for_element((By.ID, 'newButtonName'))
        new_text = "NewTest"
        input_field.send_keys(new_text)

        update_button = wait_for_element((By.ID, 'updatingButton'))
        update_button.click()

        updated_text = update_button.text
        if updated_text == new_text:
            print(f"The button text is '{updated_text}' and matches the input text.")
        else:
            print(f"The button text is '{updated_text}' and does not match '{new_text}'.")

    finally:
        driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()

    visibility_test()
    progress_bar_test()
    input_text_test()
