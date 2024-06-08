from Helpers.basic_page import BasicHelper  # Importing BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
from selenium.webdriver.common.keys import Keys  # Importing Keys class for keyboard interactions
import logging  # Importing the logging module for logging messages


class Home_Page(BasicHelper):  # Define the Home_Page class which extends BasicHelper
    # Locators for elements on the home page
    btn_login_loc = (By.XPATH, "//a[@href='/login']")  # Locator for the login button
    user_action_loc = (By.XPATH, "//a[@href='/user_action']")  # Locator for the user action button

    def click_login_btn(self):
        btn_login = self.find_and_click(self.btn_login_loc)  # Find and click the login button
        logging.info("Clicked Login button")  # Log a message indicating the login button was clicked
        return btn_login  # Return the element

    def click_user_action_btn(self):
        btn_user_action = self.find_and_click(self.user_action_loc)  # Find and click the user action button
        logging.info("Clicked User_Action button")  # Log a message indicating the user action button was clicked
        return btn_user_action  # Return the element

   
