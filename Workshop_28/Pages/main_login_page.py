from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging


class Main_Login_Page(BasicHelper):
    email_loc = (By.XPATH, "//*[@id='email']")
    code_loc = (By.XPATH, "//*[@id='code']")
    btn_send_loc = (By.XPATH, "//*[@id='Send']")

    def fill_and_submit_login_form(self, email, code):
        email_fld = self.find_and_send_keys(self.email_loc, email)
        code_fld = self.find_and_send_keys(self.code_loc, code)
        btn_send = self.find_and_click(self.btn_send_loc)
        logging.info("Filled  email, code, and clicked Send button")
        return email_fld, code_fld, btn_send