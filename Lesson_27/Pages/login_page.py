from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class Login_Page(BasicHelper):
    email_fld_loc = (By.XPATH, "//input[@placeholder='Email Address']")
    pass_fld_loc = (By.XPATH, "//input[@id='login-password']")
    btn_login_loc = (By.XPATH, "//button[@id='login']")
    msg_valid_loc = (By.XPATH, "//span[@id='incorrectdetails']")
      
    def fill_and_submit_login_form(self, email, password):
        email_fld = self.find_and_send_keys(self.email_fld_loc, email)
        pass_fld = self.find_and_send_keys(self.pass_fld_loc, password)
        login_btn = self.find_and_click(self.btn_login_loc)
        logging.info("Filled incorrect email and password, and clicked LogIn button")
        return email_fld, pass_fld, login_btn

    def validation_message(self):
        valid_msg = self.find_elem_ui(self.msg_valid_loc).text
        logging.info(f"Validation message: {valid_msg}")
