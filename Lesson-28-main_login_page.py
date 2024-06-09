from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging


class MainLoginPage(BasicHelper):
    email_loc = (By.XPATH, "//*[@id='email']")
    code_loc = (By.XPATH, "//*[@id='code']")
    btn_send_loc = (By.XPATH, "//*[@id='Send']")

    def fill_and_submit_login_form(self, email, password):
        self.find_and_send_keys(self.email_loc, email)
        self.find_and_send_keys(self.code_loc, password)
        self.find_and_click(self.btn_send_loc)
        logging.info("Filled incorrect email and code, and clicked Send button")