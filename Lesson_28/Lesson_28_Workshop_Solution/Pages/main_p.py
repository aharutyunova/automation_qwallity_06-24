from Helpers import basic_page
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import logging


email_loc = (By.XPATH, '//*[@id="email"]')
code_loc = (By.XPATH, '//*[@id="code"]')
btn_send_loc = (By.XPATH, '//*[@id="Send"]')


# def authorization(driver, email, code):
#     email_el = basic_page.find_elem_ui(driver, email_loc)
#     email_el.send_keys(email)

#     code_el = basic_page.find_elem_ui(driver, code_loc)
#     code_el.send_keys(code)

#     btn_send_el = basic_page.find_elem_ui(driver, btn_send_loc)
#     btn_send_el.send_keys(Keys.ENTER)
#     logging.info('Send button clicked')


def authorization(driver, email, code):
    try:
        logging.info("Starting authorization process")

        basic_page.find_and_send_keys(driver, email_loc, email)
        logging.info(f"Email entered: {email}")

        basic_page.find_and_send_keys(driver, code_loc, code)
        logging.info(f"Code entered: {code}")

        basic_page.find_and_click(driver, btn_send_loc)
        logging.info("Send button clicked")
    except Exception as e:
        logging.error(f"Error during authorization: {e}")
