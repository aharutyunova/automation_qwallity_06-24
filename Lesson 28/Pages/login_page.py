from Helpers.basic_page import BasicHelper  # Importing the BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
from selenium.webdriver.common.keys import Keys  # Importing Keys class for keyboard interactions
import logging  # Importing the logging module for logging messages

class Login_Page(BasicHelper):  # Define the Login_Page class which extends BasicHelper
   
    # Define locators for various elements on the page
    username_loc = (By.XPATH, "//input[@id='username']")  # Locator for the username field
    password_loc = (By.XPATH, "//input[@id='password-field']")  # Locator for the password field
    btn_log_in_loc = (By.XPATH, "//button[@class='btn btn-primary']")  # Locator for the login button

    def fill_and_submit_second_login_form(self, username, password):
        # Fill the username field
        username_fld = self.find_and_send_keys(self.username_loc, username)
        # Fill the password field
        pass_fld = self.find_and_send_keys(self.password_loc, password)
        # Click the login button
        btn_log_in = self.find_and_click(self.btn_log_in_loc)
        # Log an informational message
        logging.info("Filled username, password, and clicked Log in button")
        # Return the elements involved
        return username_fld, pass_fld, btn_log_in
