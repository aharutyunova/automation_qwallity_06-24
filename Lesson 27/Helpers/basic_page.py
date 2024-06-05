from selenium.webdriver.support.ui import WebDriverWait  # Importing WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Importing expected_conditions for explicit waits
import logging  # Importing the logging module for logging messages

class BasicHelper:
    def __init__(self, driver):
        self.driver = driver  # Initializing the WebDriver instance

    def open_url(self, url):
        self.driver.maximize_window()  # Maximizing the browser window
        self.driver.get(url)  # Opening the provided URL
        logging.info(f"Open url {url}")  # Logging the URL that was opened

    def find_element_ui(self, loc, sec=10):
        element = WebDriverWait(self.driver, sec).until(  # Waiting for a specific condition (visibility of element)
            EC.visibility_of_element_located(loc))
        return element  # Returning the located element

    def find_elements(self, loc, sec=10):
        elements = WebDriverWait(self.driver, sec).until(  # Waiting for a specific condition (visibility of any elements)
            EC.visibility_of_any_elements_located(loc))
        return elements  # Returning the located elements

    def find_element_dom(self, loc, sec=10):
        element = WebDriverWait(self.driver, sec).until(  # Waiting for a specific condition (presence of element)
            EC.presence_of_element_located(loc))
        return element  # Returning the located element

    def find_and_click(self, loc, sec=10):
        element = WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc))  # Waiting for an element to be clickable
        element.click()  # Clicking on the located element

    def find_and_send_keys(self, loc, inp_text, sec=10):
        element = self.find_element_ui(loc, sec)  # Locating an element
        element.send_keys(inp_text)  # Sending keys to the located element
