from Helpers.basic_page import Basic_Hepler
from selenium.webdriver.common.by import By
import config
import logging

class Main_Page(Basic_Hepler):

    inp_email = (By.XPATH, '//input[@id="email"]')
    inp_code = (By.XPATH, '//input[@id="code"]')
    btn_send = (By.XPATH, '//button[@id="Send"]')
    btn_login = (By.XPATH, '//a[text()="Login"]')

    def enter_to_qwallity(self):
        self.find_and_send_keys(self.inp_email, config.email)
        self.find_and_send_keys(self.inp_code, config.code)
        self.find_and_click(self.btn_send)
        self.wait_for_element(self.btn_login) 
        logging.info("Enter to qwallity page successfully")
    
    def go_to_page(self, page):
        page_loc = (By.XPATH, f'//a[text()="{page}"]')
        self.find_and_click(page_loc)
