from basic_page import Basic_Helper
from selenium.webdriver.common.by import By
import logging


class Practice_Page(Basic_Helper):

    hidden_el = (By.XPATH, '//*[@id="hide-textbox"]')

    def hide_element(self):
        self.find_and_click(self.hidden_el)
        logging.info('Element hidden')
