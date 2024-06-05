from Helpers.basic_page import BasicHelper  # Importing the BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
import logging  # Importing the logging module for logging messages

class Python_Page(BasicHelper):  # Define the Python_Page class which extends BasicHelper
   
    fld_search_loc = (By.ID, "id-search-field")  # Locator for the search field
    btn_search_loc = (By.ID, "submit")  # Locator for the search button
    results_loc = (By.XPATH, '//div[@id="content"]//li')  # Locator for the search results

    def open_new_tab_and_search(self, new_tab_url, word):
        self.driver.execute_script("window.open('')")  # Execute JavaScript to open a new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the newly opened tab
        logging.info("Opened a new tab and switched to it")  # Log a message
        self.driver.get(new_tab_url)  # Navigate to the provided URL in the new tab
        logging.info("Navigated to https://www.python.org/ on the second tab")  # Log a message
        self.find_and_send_keys(self.fld_search_loc, word)  # Find the search field and enter the provided word
        self.find_and_click(self.btn_search_loc)  # Find the search button and click it
        logging.info("Searched for the word 'Automation'")  # Log a message

        results_amount = self.find_elements(self.results_loc)  # Find all elements matching the search results locator
        logging.info(f"Number of results found on the first page: {len(results_amount)}")  # Log the number of search results found
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original tab
        logging.info("Switched back to the first tab")  # Log a message
