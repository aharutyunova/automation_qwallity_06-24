from Helpers.basic_page import Basic_Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class Main_Page(Basic_Helper):

    search_input = (By.ID, 'searchbox_input')

    def search_word(self, word):
        inp_field = self.find_elem_ui(self.search_input)
        inp_field.send_keys(word + Keys.ENTER)
        logging.info(f'Search result of {word}')
