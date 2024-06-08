from Helpers.basic_page import BasicHelper  # Importing the BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
import logging  # Importing the logging module for logging messages


class Main_Page(BasicHelper):  # Define the Main_Page class which extends BasicHelper
    
    # Define locators for various elements on the page
    email_loc = (By.XPATH, "//*[@id='email']")  # Locator for the email field
    code_loc = (By.XPATH, "//*[@id='code']")  # Locator for the code field
    btn_send_loc = (By.XPATH, "//*[@id='Send']")  # Locator for the Send button

    def fill_and_submit_login_form(self, email, code):
        # Find the email field and send keys (enter email)
        email_fld = self.find_and_send_keys(self.email_loc, email)
        # Find the code field and send keys (enter code)
        code_fld = self.find_and_send_keys(self.code_loc, code)
        # Find and click the Send button
        btn_send = self.find_and_click(self.btn_send_loc)
        # Log an informational message
        logging.info("Filled email, code, and clicked Send button")
        # Return the elements involved
        return email_fld, code_fld, btn_send
