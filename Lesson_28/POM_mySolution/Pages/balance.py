from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging
import time

class Balance(Basic_Helper):

    user_action_button = (By.XPATH,"//a[@href= '/user_action']")
    accbalance_loc = (By.XPATH, "//input[@id='acc_balance']")
    amount_loc = (By.XPATH, "//input[@id='amount']")
    checkout_loc =(By.XPATH,"//button[@id='Submit']")
    payment_loc = (By.XPATH,"//select[@id='payment' ]/option[@value='1']")

    
    def addBalance(self, amount_data):
        self.findandinput(self.amount_loc, amount_data)
        self.findandclick(self.payment_loc)
        self.findandclick(self.checkout_loc)
        logging.info("amount successfully added")
        
    def getElementValue(self, loc):
        time.sleep(2)
        elem = self.locelement(loc)
        value = elem.get_attribute('value')
        logging.info("Element value get")
        return float(value)
    