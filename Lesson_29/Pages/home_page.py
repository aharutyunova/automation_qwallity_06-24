from selenium.webdriver.common.by import By
from Lesson_29.Helpers.base_page import BasePage
import logging


class HomePage(BasePage):
    input_fld_loc = (By.XPATH, "//*[@id='searchInp-small']")
    search_btn_loc = (By.XPATH, "//*[@id='submit_search-small']")
    search_results_loc = (By.XPATH, "//*[@id='research-btn']/span")

    def enter_search_key(self, key):
        self.find_and_send_keys(self.input_fld_loc, key)
        logging.info(f'Search result for {key}')

    def click_search_btn(self):
        self.find_and_click(self.search_btn_loc)

    def get_result(self):
        res = self.find_elements(self.search_results_loc)
        logging.info(f"Number of results: {res[0].text}")
        return res[0].text