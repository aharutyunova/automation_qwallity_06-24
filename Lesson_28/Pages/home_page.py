from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time


class Home_Page(BasicHelper):
    btn_login_loc = (By.XPATH, "//a[@href='/login']")
    user_action_loc = (By.XPATH, "//a[@href='/user_action']")

    def click_login(self):
        btn_login = self.find_and_click(self.btn_login_loc)
        logging.info("Clicked Login button")
        return btn_login

    def click_user_action_btn(self):
        btn_user_action = self.find_and_click(self.user_action_loc)
        logging.info("Clicked User_Action button")
        return btn_user_action
    time.sleep(3)
    
