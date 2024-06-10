from Helpers.basic_page import Basic_Hepler
from selenium.webdriver.common.by import By
import config
import logging

class Login_Page(Basic_Hepler):

    inp_username = (By.XPATH, '//input[@id="username"]')
    inp_password = (By.XPATH, '//input[@id="password-field"]')
    btn_submit = (By.XPATH, "//button[@type='submit']")
    btn_login = (By.XPATH, '//a[text()="Login"]')
    lnk_user_action = (By.XPATH, '//a[text()="User_Action"]')

    def login(self):
        self.find_and_click(self.btn_login)
        self.find_and_send_keys(self.inp_username, config.username)
        self.find_and_send_keys(self.inp_password, config.password)
        self.find_and_click(self.btn_submit)
        self.wait_for_element(self.lnk_user_action)
        logging.info("Login to the system")
