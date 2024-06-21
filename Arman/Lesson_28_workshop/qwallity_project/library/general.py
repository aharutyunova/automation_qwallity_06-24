import logging

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.driver import driver

action = ActionChains(driver)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w+',
    encoding='utf-8'
)


def run_driver(driver, url):
    """Function run web browser driver with given URL"""
    try:
        driver.get(url)
        driver.maximize_window()
        logging.info(f"{driver.name} web driver successfully ran and opened {url} page")
    except TimeoutError as error:
        logging.error(error)


def click_on_button(driver, button_xpath):
    try:
        # Wait for the button to be clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        # Perform the click action
        button.click()
        logging.info(f"{button_xpath} button successfully clicked")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def wait(input_driver, seconds):
    """Function stops application with fixed seconds"""
    input_driver.implicitly_wait(seconds)


def get_style_attribute(input_xpath):
    input_field_xpath = driver.find_element(By.XPATH, input_xpath)
    style = input_field_xpath.get_attribute('style')
    return style


def fill_form(email_input_xpath, password_input_xpath, email, password):
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, email_input_xpath))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, password_input_xpath))
        )

        # Input the email and password
        email_input.send_keys(email)
        password_input.send_keys(password)
        logging.info("Email and password successfully filled")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def close_browser(input_driver):
    """Function close tabs and browser"""
    try:
        input_driver.quit()
        logging.info(f"{driver.name} browser successfully closed")
    except Exception as e:
        logging.error(e)