from Helpers.basic_page import BasicHelper  # Importing BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
from selenium.webdriver.common.keys import Keys  # Importing Keys class for keyboard interactions
import logging  # Importing the logging module for logging messages


class Brands_Page(BasicHelper):

    search_input_loc = (By.XPATH, "//input[@id='searchInp']")
    search_result_loc = (By.XPATH, "//div[@id='search-result']/div")

    def search_a_brand(self, car_brand):
        search_input = self.find_element_ui(self.search_input_loc)
        search_input.clear()
        search_input.send_keys(car_brand)
        search_input.send_keys(Keys.RETURN) 
        logging.info(f"Searching for car brand: {car_brand}")

    def get_results_count(self):
        logging.info("Getting search results")
        search_results = self.find_elements(self.search_result_loc)
        logging.info(f"Search results on one page:: {len(search_results)}")
        return search_results

 