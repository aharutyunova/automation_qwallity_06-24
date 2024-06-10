from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By
import logging


class First_Login(Basic_Helper):
    email_loc = (By.XPATH, "//input[@id='email']")
    code_loc = (By.XPATH, "//input[@id='code']")
    send_loc = (By.XPATH, "//button[@id = 'Send']")
    navigation_bar_login = (By.XPATH, "//a[@href= '/login']")

    def firstLogin(self, email_data, code_data):
        self.findandinput(self.email_loc, email_data)
        self.findandinput(self.code_loc, code_data)
        self.findandclick(self.send_loc)
        logging.info("Successfully passed first login")
    

    


