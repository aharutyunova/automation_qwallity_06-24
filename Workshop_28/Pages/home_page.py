from Workshop_28.Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging


class HomePage(BasicHelper):
    btn_login_loc = (By.XPATH, "//a[@href='/login']")
    user_action_loc = (By.XPATH, "//a[@href='/user_action']")

    def click_login(self):
        btn_login = self.find_and_click(self.btn_login_loc)
        logging.info("Login button is clicked")
        return btn_login

    def click_user_action_btn(self):
        btn_user_action = self.find_and_click(self.user_action_loc)
        logging.info("User Acction button is clicked")
        return btn_user_action

