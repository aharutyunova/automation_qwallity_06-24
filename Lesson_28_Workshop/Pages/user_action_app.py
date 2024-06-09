from Helpers import basic_page
from selenium.webdriver.common.by import By
import logging
import time

# User action locators
account_balance = (By.ID, 'acc_balance')
amount_field = (By.ID, 'amount')
checkout_button = (By.ID, 'Submit')

try:
    def add_amount(driver, amount):
        basic_page.find_and_send_keys(driver, amount_field, amount)
        basic_page.find_and_click(driver, checkout_button)
        time.sleep(2)

    def get_balance(driver):
        time.sleep(1)
        acc_balance = basic_page.find_elem_ui(
            driver, account_balance).get_attribute('value')
        return acc_balance

except Exception as e:
    logging.error(f"Error {e}")
