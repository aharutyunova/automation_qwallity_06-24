from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class Basic_Helper:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        logging.info(f"Opened URL {url}")

    def find_elem_ui(self, loc, sec=10):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.visibility_of_element_located(loc))
            return elem
        except Exception as e:
            logging.error(f"Error finding element in UI: {str(e)}")
            raise

    def find_elements(self, loc, sec=10):
        try:
            elements = WebDriverWait(self.driver, sec).until(
                EC.visibility_of_any_elements_located(loc))
            return elements
        except Exception as e:
            logging.error(f"Error finding elements: {str(e)}")
            raise

    def find_elem_dom(self, loc, sec=10):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.presence_of_element_located(loc))
            return elem
        except Exception as e:
            logging.error(f"Error finding element in DOM: {str(e)}")
            raise

    def find_and_click(self, loc, sec=10):
        try:
            elem = WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            self.driver.execute_script("arguments[0].click();", elem)
            return elem
        except Exception as e:
            logging.error(f"Error finding and clicking element: {str(e)}")
            raise

    def find_and_send_keys(self, loc, inp_text, sec=10):
        try:
            elem = self.find_elem_ui(loc, sec)
            elem.send_keys(inp_text)
            return elem
        except Exception as e:
            logging.error(f"Error finding element and sending keys: {str(e)}")
            raise

    def close_driver(self):
        try:
            self.driver.quit()
            logging.info("Driver and all opened tabs are closed")
        except Exception as e:
            logging.error(f"Error closing driver: {str(e)}")
            raise

    def find_and_click(self, loc, sec=10):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.element_to_be_clickable(loc)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            self.driver.execute_script("arguments[0].click();", elem)
            return elem
        except Exception as e:
            logging.error(f"Error finding and clicking element: {str(e)}")
            raise
