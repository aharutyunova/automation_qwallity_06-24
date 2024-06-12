from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasicHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        logging.info(f"Open url {url}")

    def find_elem_ui(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(
            EC.visibility_of_element_located(loc))
        return elem

    def find_elements(self, loc, sec=10):
        elements = WebDriverWait(self.driver, sec).until(
            EC.visibility_of_any_elements_located(loc))
        return elements

    def find_elem_dom(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(
            EC.presence_of_element_located(loc))
        return elem

    def find_and_click(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc))
        elem.click()

    def find_and_send_keys(self, loc, inp_text, sec=10):
        elem = self.find_elem_ui(loc, sec)
        elem.send_keys(inp_text)
