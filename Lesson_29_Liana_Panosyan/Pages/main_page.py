from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging
import time


class AutoPage(BasicHelper):
    search_input = (By.ID, "searchInp")
    search_button = (By.ID, "submit_search")
    search_result = (By.XPATH, "//div[@id='search-result']/div")

    def search_car(self, car_name):
        search_input = self.find_elem_ui(self.search_input)
        search_input.clear()
        search_input.send_keys(car_name)
        self.find_and_click(self.search_button)
        time.sleep(3)
        logging.info(f"Searching for car brand: {car_name}")

    def get_result(self):
        time.sleep(1)
        search_results = self.find_elements(self.search_result)
        time.sleep(2)
        logging.info(f"Search results on one page:: {len(search_results)}")
        return search_results
