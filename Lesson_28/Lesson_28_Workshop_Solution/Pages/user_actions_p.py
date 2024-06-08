from selenium.webdriver.common.by import By
from Helpers import basic_page
import logging
import time

get_balance = (By.XPATH, '//*[@id="acc_balance"]')
inp_amount = (By.XPATH, '//*[@id="amount"]')
btn_chackout = (By.XPATH, '//*[@id="Submit"]')

try:
    def get_acc_balance(driver):
        time.sleep(1)
        acc_balance = basic_page.find_elem_ui(
            driver, get_balance).get_attribute('value')
        return acc_balance

    def payment(driver, amount):
        basic_page.find_and_send_keys(driver, inp_amount, amount)
        basic_page.find_and_click(driver, btn_chackout)
except Exception as e:
    logging.error(f"Error on get balance or performing payment: {e}")
