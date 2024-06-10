from Helpers.basicHelper import Basic_Helper
from Helpers import locators
import testdata

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class Second_Login(Basic_Helper):
    # First login XPath
    username_loc = (By.XPATH, "//input[@id='username']")
    password_loc = (By.XPATH, "//input[@id='password-field']")
    login_loc = (By.XPATH, "//button[@type = 'submit']")
    
    def secondLogin(self, username_data, password_data):
        self.findandinput(self.username_loc, username_data)
        self.findandinput(self.password_loc, password_data)
        self.findandclick(self.login_loc)
        logging.info("Successfully passed second login")
    