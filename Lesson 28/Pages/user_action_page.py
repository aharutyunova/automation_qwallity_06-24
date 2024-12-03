from Helpers.basic_page import BasicHelper  # Importing the BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
import logging  # Importing the logging module for logging messages
import time  # Importing the time module for adding delays

class User_Action_Page(BasicHelper):  # Define the User_Action_Page class which extends BasicHelper

    # Define locators for various elements on the page
    fld_amount_loc = (By.XPATH, "//input[@id='amount']")  # Locator for the amount field
    btn_checkout_loc = (By.XPATH, "//button[@id='Submit']")  # Locator for the Checkout button
    account_balance_loc = (By.XPATH, "//input[@id='acc_balance']")  # Locator for the account balance field
    
    def get_balance(self):
        # Add a 1-second delay to ensure the element is loaded
        time.sleep(1)
        # Find the account balance field and get its 'value' attribute
        acc_bal = self.find_element_ui(self.account_balance_loc).get_attribute('value')
        # Return the account balance
        return acc_bal

    def add_amount_and_submit_checkout_btn(self, amount):
        # Find the amount field and enter the provided amount
        fld_amount = self.find_and_send_keys(self.fld_amount_loc, amount)
        # Find and click the Checkout button
        btn_checkout = self.find_and_click(self.btn_checkout_loc)
        # Log an informational message
        logging.info(f"{amount} amount is added and clicked Checkout button")
        # Return the elements involved
        return fld_amount, btn_checkout
