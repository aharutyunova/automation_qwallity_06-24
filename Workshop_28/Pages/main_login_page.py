import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from Workshop_28.Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging


class Main_Login_page(BasicHelper):
    email_loc = (By.XPATH, "//*[@id='email']")
    code_loc = (By.XPATH, "//*[@id='code']")
    btn_send_loc = (By.XPATH, "//*[@id='Send']")

    def fill_and_submit_login_form(self, email, password):
        email_fld = self.find_and_send_keys(self.email_loc, email)
        code_fld = self.find_and_send_keys(self.code_loc, password)
        btn_send = self.find_and_click(self.btn_send_loc)
        logging.info("Filled incorrect email and code, and clicked Send button")
        return email_fld, code_fld, btn_send
