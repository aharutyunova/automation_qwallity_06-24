from Lesson_27.Helpers.basic_page import Basic_Helper
from selenium.webdriver.common.by import By
import logging


class Result_Page(Basic_Helper):
    results = (By.XPATH, '//article[@data-testid="result"]')
    inp_field = (By.ID, 'search_form_input')

    def get_result(self):
        res = self.find_elements(self.results)
        logging.info(f"Number of results: {len(res)}")
        return len(res)


    def get_search_input_value(self):
        search_field_value = self.find_elem_ui(self.inp_field).get_attribute('value')
        logging.info(f"Search input value: {search_field_value}")
        return search_field_value