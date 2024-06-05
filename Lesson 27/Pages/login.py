from Helpers.basic_page import BasicHelper  # Importing the BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
from selenium.webdriver.common.keys import Keys  # Importing Keys class for keyboard interactions
import logging  # Importing the logging module for logging messages

class Login_Page(BasicHelper):  # Define the Login_Page class which extends BasicHelper
   
    email_fld_loc = (By.ID, "email")  # Locator for the email field
    password_fld_loc = (By.ID, "login-password")  # Locator for the password field
    btn_login_loc = (By.ID, "login")  # Locator for the login button
    msg_valid_loc = (By.ID, 'incorrectdetails')  # Locator for the validation message
    
    def fill_and_submit_login_form(self, email, password):
        email_fld = self.find_and_send_keys(self.email_fld_loc, email)  # Find the email field and send keys (email)
        pass_fld = self.find_and_send_keys(self.password_fld_loc, password)  # Find the password field and send keys (password)
        login_btn = self.find_and_click(self.btn_login_loc)  # Find the login button and click it
        logging.info("Filled incorrect email and password, and clicked LogIn button")  # Log a message
        return email_fld, pass_fld, login_btn  # Return elements for potential further use

    def validation_message(self):
        valid_msg = self.find_element_ui(self.msg_valid_loc).text  # Find the validation message element and get its text
        logging.info(f"Validation message: {valid_msg}")  # Log the validation message
