from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging
import time


class User_Action_Page(BasicHelper):
    fld_amount_loc = (By.XPATH, "//input[@id='amount']")
    btn_checkout_loc = (By.XPATH, "//button[@id='Submit']")
    account_balance_loc = (By.XPATH, "//input[@id='acc_balance']")
    
    def get_balance(self):
        time.sleep(1)
        acc_bal = self.find_elem_ui(self.account_balance_loc).get_attribute('value')
        return acc_bal

    def add_ammoun_and_submit_checkout_btn(self, amount):
        fld_amount = self.find_and_send_keys(self.fld_amount_loc, amount)
        btn_checkout = self.find_and_click(self.btn_checkout_loc)
        logging.info(f"{amount} ammount is added and clicked Checkout button")
        return fld_amount, btn_checkout