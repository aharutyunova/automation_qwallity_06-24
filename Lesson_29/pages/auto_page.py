from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
import logging
import time


class Auto_Page(BasicHelper):
    search_input_loc = (By.XPATH, "//input[@id='searchInp']")
    btn_search_loc = (By.XPATH, "//i[@id='submit_search']")
    search_result_loc = (By.XPATH, "//div[@id='search-result']/div")

    def search_car(self, car_brand):
        search_input = self.find_elem_ui(self.search_input_loc)
        search_input.clear()
        search_input.send_keys(car_brand)
        time.sleep(1)
        self.find_and_click(self.btn_search_loc)
        logging.info(f"Searching for car brand: {car_brand}")
    
    # def search_car(self, car_brand):
    #     search_input = self.find_and_send_keys(self.search_input_loc, car_brand)
    #     time.sleep(1)
    #     btn_search = self.find_and_click(self.btn_search_loc)
    #     logging.info(f"Searching for car brand: {car_brand}")
    #     return search_input, btn_search

    def get_results_count(self):
        time.sleep(1)
        logging.info("Getting search results")
        search_results = self.find_elements(self.search_result_loc)
        logging.info(f"Search results on one page:: {len(search_results)}")
        return search_results
