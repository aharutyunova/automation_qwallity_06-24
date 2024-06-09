from selenium.webdriver.common.by import By
from Helpers import basic_page
import logging

# Locators for Login page.
username_field = (By.ID, 'username')
password_field = (By.ID, 'password-field')
login_button = (By.XPATH, '//*[contains(text(), "Log in")]')


def login_system(driver, username, password):
    try:
        basic_page.find_and_send_keys(driver, username_field, username)
        basic_page.find_and_send_keys(driver, password_field, password)
        basic_page.find_and_click(driver, login_button)
        logging.info("Successful login")
    except Exception as e:
        logging.error(f"Error during login: {e}")
