from Helpers import basic_page
from selenium.webdriver.common.by import By
import logging

# Locators for Enter app page.
email_field = (By.ID, 'email')
code_field = (By.ID, 'code')
send_button = (By.ID, 'Send')


def authorization(driver, email, code):
    try:
        basic_page.find_and_send_keys(driver, email_field, email)
        basic_page.find_and_send_keys(driver, code_field, code)
        basic_page.find_and_click(driver, send_button)
    except Exception as e:
        logging.error(f"Error during authorization: {e}")
