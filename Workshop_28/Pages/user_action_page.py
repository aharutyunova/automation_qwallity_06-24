from Workshop_28.Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging
import time


class UserActionPage(BasicHelper):
    account_balance_fld_loc = (By.XPATH, "//*[@id='acc_balance']")
    amount_fld_loc = (By.XPATH, "//*[@id='amount']")
    payment_method_fld_loc = (By.XPATH, "//*[@id='payment']")
    btn_checkout_loc = (By.XPATH, "//*[@id='Submit']")

    def get_balance(self):
        time.sleep(1)
        return self.find_elem_ui(self.account_balance_fld_loc).get_attribute("value")

    def add_amount_and_submit_checkout_btn(self, amount):
        self.find_and_send_keys(self.amount_fld_loc, amount)
        self.find_and_click(self.btn_checkout_loc)
        logging.info(f"{amount} amount is added and Checkout button is clicked")


