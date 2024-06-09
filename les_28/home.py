import general
from selenium.webdriver.common.by import By
import logging


btn_login = (By.XPATH, '//a[@href="/login"]')
btn_user_action = (By.XPATH, '//*[@href="/user_action"]')

try:
    def go_to_login_form(driver):
        general.find_and_click(driver, btn_login)
        logging.info("Login page")

    def go_to_user_actions(driver):
        general.find_and_click(driver, btn_user_action)
        logging.info("User_action page")
except Exception as e:
    logging.error(
        f"Error during redirect to the 'login' or 'user_action' pages: {e}")