from selenium.webdriver.common.by import By
from Helpers import basic_page
import logging
import time

inp_email_loc = (By.XPATH, '//*[@id="email"]')
inp_pass_loc = (By.XPATH, '//*[@id="login-password"]')
btn_login_loc = (By.XPATH, '//*[@id="login"]')
msg_login_loc = (By.XPATH, '//*[@id="incorrectdetails"]')


def login(driver, email, password):
    try:
        basic_page.find_and_send_keys(driver, inp_email_loc, email)
        basic_page.find_and_send_keys(driver, inp_pass_loc, password)
        basic_page.find_and_click(driver, btn_login_loc)

        time.sleep(1)
        msg_login = basic_page.find_elem_ui(driver, msg_login_loc)
        if msg_login:
            logging.info(msg_login.text)
        else:
            logging.error("Login message element not found.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
