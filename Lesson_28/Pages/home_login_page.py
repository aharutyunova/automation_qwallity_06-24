from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class Home_Login_Page(BasicHelper):
    username_loc = (By.XPATH, "//input[@id='username']")
    password_loc = (By.XPATH, "//input[@id='password-field']")
    btn_log_in_loc = (By.XPATH, "//button[@class='btn btn-primary']")

    def fill_and_submit_second_login_form(self, username, password):
        username_fld = self.find_and_send_keys(self.username_loc, username)
        pass_fld = self.find_and_send_keys(self.password_loc, password)
        btn_log_in = self.find_and_click(self.btn_log_in_loc)
        logging.info("Filled  username, password, and clicked Log in button")
        return username_fld, pass_fld, btn_log_in
