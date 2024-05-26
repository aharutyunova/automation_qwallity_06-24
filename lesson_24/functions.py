from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


def visibilty():
    try:
        driver.get('http://www.uitestingplayground.com/')
        time.sleep(2)

        visibility_link = driver.find_element(By.LINK_TEXT, 'Visibility')
        visibility_link.click()
        time.sleep(2)

        button_hide = driver.find_element(By.XPATH, '//*[@id="hideButton"]')
        button_hide.click()
        time.sleep(2)

        buttons = driver.find_elements(By.XPATH, '//button[@class="btn-primary"]')
        hidden = all(not button.is_displayed() for button in buttons)

        if hidden:
            print("Great:All buttons are hidden.")
        else:
            print("Fail: Some buttons are still visible.")

    finally:
        driver.quit()


def progres_bar():
    try:
        driver.get('http://www.uitestingplayground.com/')
        time.sleep(5)

        progress_bar_link = driver.find_element(By.LINK_TEXT, 'Progress Bar')
        progress_bar_link.click()
        time.sleep(2)

        start_button = driver.find_element(By.XPATH, '//*[@id="startButton"]')
        start_button.click()

        time.sleep(5)

        stop_button = driver.find_element(By.XPATH, '//*[@id="stopButton"]')
        stop_button.click()

        duration_element = driver.find_element(By.XPATH, '//*[@id="result"]')
        duration = duration_element.text

        print(f"Duration: {duration}")

    finally:
        driver.quit()
        

def input_text():
    try:
        driver.get('http://www.uitestingplayground.com/')
        time.sleep(5)

        progress_bar_link = driver.find_element(By.LINK_TEXT, 'Text Input')
        progress_bar_link.click()
        time.sleep(2)

        start_button = driver.find_element(By.XPATH, '//*[@id="newButtonName"]')
        new_text = "NewTest"
        start_button.send_keys(new_text)
        time.sleep(5)

        button1 = driver.find_element(By.XPATH, '//*[@id="updatingButton"]')
        button1.click()

        updated = button1.text
        if updated == new_text:
            print(f"Success: The button text is '{updated}' and matches the in text.")
        else:
            print(f"Failure: The button text is '{updated}' and does not match the in text '{new_text}'.")

    finally:
        driver.quit()
