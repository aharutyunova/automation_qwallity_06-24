from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging


class Python_Page(BasicHelper):

    fld_search_loc = (By.XPATH, "//input[@id='id-search-field']")
    btn_search_loc = (By.XPATH, "//button[@id='submit']")
    results_loc = (By.XPATH, '//div[@id="content"]//li')

    def open_new_tab_and_search(self, new_tab_url, word):
        self.driver.execute_script("window.open('')")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logging.info("Opened a new tab and switched to it")
        self.driver.get(new_tab_url)
        logging.info("Navigated to https://www.python.org/ on the second tab")
        self.find_and_send_keys(self.fld_search_loc, word)
        self.find_and_click(self.btn_search_loc)
        logging.info("Searched for the word 'Automation'")

        results_el = self.find_elements(self.results_loc)
        logging.info(f"Number of results found on the first page: {len(results_el)}")
        self.driver.switch_to.window(self.driver.window_handles[0])
        logging.info("Switched back to the first tab")
