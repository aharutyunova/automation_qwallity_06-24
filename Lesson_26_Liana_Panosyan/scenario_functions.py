from selenium.webdriver.common.keys import Keys
import locators
import test_data
import general
import logging
import os
import time

script_directory = os.path.dirname(os.path.abspath(__file__))
log_file = "my_log.log"
log_file_path = os.path.join(script_directory, log_file)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=log_file_path,
    filemode="w+",
    encoding="utf-8",
)


def alert_text(driver):
    general.find_and_click(driver, locators.alert_button)
    alert = driver.switch_to.alert
    alert_text = alert.text
    logging.info(f"Alert text: {alert_text}")
    alert.accept()


def hide_element(driver):
    general.find_and_click(driver, locators.hide_button)
    hide_attr = general.find_element_dom(
        driver, locators.element_to_hide
    ).get_attribute("style")
    logging.info(f"Element hidden: {hide_attr}")


def mouse_hover(driver):
    general.find_and_click(driver, locators.mouse_hover_button)
    general.find_and_click(driver, locators.top_option)


def footer_text(driver):
    general.find_element_ui(driver, locators.footer)
    footer_text = general.find_element_dom(driver, locators.footer).text
    logging.info(f"Footer text: {footer_text}")


def sign_in(driver):
    time.sleep(2)
    general.find_and_click(driver, locators.sign_in_button)
    general.find_and_send_keys(driver, locators.email_address, test_data.email)
    general.find_and_send_keys(driver, locators.password, test_data.password)
    general.find_and_click(driver, locators.login_button)
    validation_message = general.find_element_ui(
        driver, locators.validation_error, 10
    ).text
    logging.info(f"Validation error message: {validation_message}")


def python_search(driver):
    driver.execute_script("window.open('https://www.python.org', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    general.find_and_send_keys(
        driver, locators.search_input_field, test_data.search_data
    )
    general.find_element_dom(driver, locators.search_input_field).send_keys(Keys.ENTER)
    found_result = general.find_elements(driver, locators.search_result)
    logging.info(f"Number of automation mentions: {len(found_result)}")

    driver.switch_to.window(driver.window_handles[0])
