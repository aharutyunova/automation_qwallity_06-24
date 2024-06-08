from Helpers import basic_page
from selenium.webdriver.common.by import By
import logging


inp_username = (By.XPATH, '//*[@id="username"]')
inp_password = (By.XPATH, '//*[@id="password-field"]')
btn_login = (By.XPATH, '//*[contains(text(), "Log in")]')

try:
    def login(driver, username, password):
        basic_page.find_and_send_keys(driver, inp_username, username)
        logging.info(f"Username entered: {username}")

        basic_page.find_and_send_keys(driver, inp_password, password)
        logging.info(f"Password entered: {password}")

        basic_page.find_and_click(driver, btn_login)
        logging.info("Login button clicked")
except Exception as e:
    logging.error(f"Error during login: {e}")
