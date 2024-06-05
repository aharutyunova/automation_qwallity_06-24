from Helpers.basic_practice import Basic_Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class Login_Page(Basic_Helper):

    email = (By.XPATH, "//input[@id= 'email' and @class = 'form-control input-md']")
    password = (By.XPATH, "//input[@id= 'login-password']")
    login_btn = (By.XPATH, "//button[@id = 'login']")
    incorrect_login_text_loc = (By.XPATH, "//span[@id = 'incorrectdetails']")
    
    expected_incorrect_login_text = 'Incorrect login details. Please try again.'
    
    def incorrectLogin(self, _email, _password):
        Basic_Helper.findandinput(self.driver, self.email, _email)
        Basic_Helper.findandinput(self.driver, self.password, _password)
        Basic_Helper.findandclick(self.driver, self.login_btn)