import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

WAIT_TIME = 30
logger = logging.getLogger()


def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def log_and_click(driver, locator, message):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    try:
        element.click()
        logger.info(message)
    except Exception as e:
        logger.error(f"Error clicking element: {str(e)}")
        time.sleep(1)
        element.click()
        logger.info(message)


def scroll_into_view_and_hover(driver, locator, message):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    logger.info(message)


def fill_and_submit(driver, locator, text, message):
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()  # Clear any existing text
        element.send_keys(text)
        logger.info(message)
    except Exception as e:
        logger.error(f"Error filling element: {str(e)}")
        raise


def check_element_hidden(driver, locator, assertion_message):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    assert "display: none;" in element.get_attribute("style"), assertion_message
    logger.info(assertion_message)


def search_and_count_results(driver, locator, text):
    search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    search_box.send_keys(text)
    search_box.send_keys(Keys.RETURN)
    results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list-recent-events > li")))
    num_results = len(results)
    logger.info(f"Number of search results on the first page: {num_results}")


def close_driver(driver):
    driver.quit()
    logger.info("Driver and all opened tabs are closed")


def main():
    driver = initialize_driver()

    try:
        driver.get("https://www.letskodeit.com/practice")

        # Alert button
        btn_alert_loc = (By.XPATH, "//input[@id='alertbtn']")
        log_and_click(driver, btn_alert_loc, "Clicked on Alert button")
        al = driver.switch_to.alert
        logger.info(f"Alert text: {al.text}")
        al.accept()

        # Hide button
        hide_button_loc = (By.ID, "hide-textbox")
        log_and_click(driver, hide_button_loc, "Clicked on Hide button")
        check_element_hidden(driver, (By.ID, "displayed-text"), "Element is hidden successfully")

        # Mouse Hover button
        mouse_hover_button_loc = (By.ID, "mousehover")
        scroll_into_view_and_hover(driver, mouse_hover_button_loc, "Hovered over the Mouse Hover button")

        # Clicking on Top option
        top_option_loc = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
        log_and_click(driver, top_option_loc, "Clicked on Top option")

        # Footer text
        footer_text_loc = (By.XPATH, "//*[@id='page']/div[3]/div/div/div[1]/div/div[1]/p")
        scroll_into_view_and_hover(driver, footer_text_loc, "Page is scrolled to the footer")
        footer_text = driver.find_element(*footer_text_loc).text
        logger.info(f"Footer text: {footer_text}")

        # Scrolling to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        logger.info("Page is scrolled to the top")

        # Sign In button and its actions
        sign_in_btn_loc = (By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a')
        log_and_click(driver, sign_in_btn_loc, "Clicked on Sign In button")
        time.sleep(5)  # Added time.sleep(5) after clicking sign-in button

        # Switching to Login page
        driver.switch_to.window(driver.window_handles[-1])

        # Fill incorrect email and password
        fill_and_submit(driver, (By.ID, "email"), "incorrect@email.com", "Filled incorrect email")
        fill_and_submit(driver, (By.XPATH, "//*[@id='login-password']"), "incorrectpassword", "Filled incorrect password")

        # Click Login button
        log_and_click(driver, (By.XPATH, "//*[@id='login']"), "Clicked on Login button")

        # Validation message
        validation_msg_loc = (By.ID, "incorrectdetails")
        validation_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(validation_msg_loc)).text.strip()
        logger.info(f"Validation message: {validation_text}")

        # Open new tab
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        logger.info("Switched to the new tab")

        # Go to Python.org and searching "Automation" word
        driver.get("https://www.python.org/")
        search_box_loc = (By.ID, "id-search-field")
        search_and_count_results(driver, search_box_loc, "Automation")

    finally:
        close_driver(driver)


if __name__ == "__main__":
    main()

# here I used some python logic
# and the issue  explained in workshop25.py file does not exists here, cause I made some changes