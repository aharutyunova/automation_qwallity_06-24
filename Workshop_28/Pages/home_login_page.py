from Workshop_28.Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging


class HomeLoginPage(BasicHelper):
    username_loc = (By.XPATH, "//input[@id='username']")
    password_loc = (By.XPATH, "//input[@id='password-field']")
    btn_log_in_loc = (By.XPATH, "//button[@class='btn btn-primary']")

    def fill_and_submit_new_user_login_form(self, username, password):
        username_fld = self.find_and_send_keys(self.username_loc, username)
        password_fld = self.find_and_send_keys(self.password_loc, password)
        btn_log_in = self.find_and_click(self.btn_log_in_loc)
        logging.info("Username and passwords are filled, and Log in button is clicked")
        return username_fld, password_fld, btn_log_in
