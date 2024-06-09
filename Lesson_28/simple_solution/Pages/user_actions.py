from Helpers.basic_page import Basic_Hepler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging
import testdata
import time

class User_Actions(Basic_Hepler):

    lnk_user_action = (By.XPATH, '//a[text()="User_Action"]')
    inp_acc_balance = (By.XPATH, '//input[@id="acc_balance"]')
    inp_amount = (By.XPATH, '//input[@id="amount"]')
    ddl_payment_method = (By.XPATH, '//select[@id="payment"]')
    btn_checkout = (By.XPATH, '//button[@id="Submit"]')

    def get_balance_value(self):
        time.sleep(0.5)
        amount = self.find_elem_ui(self.inp_acc_balance).get_attribute('value')
        logging.info(f"Balance Value is {amount}")
        return float(amount)

    def add_balance(self, amount):
        self.find_and_send_keys(self.inp_amount, amount)
        select = Select(self.driver.find_element(*self.ddl_payment_method))
        select.select_by_visible_text(testdata.payment_method)
        self.find_and_click(self.btn_checkout)
        logging.info(f"Balance is added with {amount}")
