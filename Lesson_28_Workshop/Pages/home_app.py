from selenium.webdriver.common.by import By
from Helpers import basic_page
import logging
# Locators for Home Page.
login_button = (By.XPATH, "//a[@href = '/login']")
user_action_button = (By.XPATH, '//a[@href="/user_action"]')

try:
    def go_to_login(driver):
        basic_page.find_and_click(driver, login_button)
        logging.info("Login page")

    def go_to_user_actions(driver):
        basic_page.find_and_click(driver, user_action_button)
        logging.info("User action page")
except Exception as e:
    logging.error(
        f"Redirection error: {e}")