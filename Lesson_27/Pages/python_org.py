from Helpers.basic_page import Basic_Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class Python_Org(Basic_Helper):
    search_input = (By.ID, "id-search-field")

    def search_word(self, word):
        inp_field = self.find_elem_ui(self.search_input)
        inp_field.send_keys(word + Keys.ENTER)
        logging.info(f'Search result for {word}')

    def python_search(self):
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logging.info("Switched to the new tab")
        self.driver.get("https://www.python.org/")
        search_box = self.find_elem_ui(self.search_input)
        search_box.send_keys("Automation")
        search_box.send_keys(Keys.RETURN)
        results = self.find_elements((By.CSS_SELECTOR, ".list-recent-events > li"))
        num_results = len(results)
        logging.info(f"Number of search results on the first page: {num_results}")
