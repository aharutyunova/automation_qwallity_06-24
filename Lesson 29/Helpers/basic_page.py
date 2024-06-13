from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import logging  

class BasicHelper:
    def __init__(self, driver):
        self.driver = driver 

    def open_base_url(self, url):
        self.driver.maximize_window() 
        self.driver.get(url)  
        logging.info(f"Open url {url}") 

    def find_element_ui(self, loc, sec=10):
        element = WebDriverWait(self.driver, sec).until(  
            EC.visibility_of_element_located(loc))
        return element 

    def find_elements(self, loc, sec=10):
        elements = WebDriverWait(self.driver, sec).until(  
            EC.visibility_of_any_elements_located(loc))
        return elements  

    def find_element_dom(self, loc, sec=10):
        element = WebDriverWait(self.driver, sec).until(  
            EC.presence_of_element_located(loc))
        return element  

    def find_and_click(self, loc, sec=10):
        element = WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc))  
        element.click() 

    def find_and_send_keys(self, loc, inp_text, sec=10):
        element = self.find_element_ui(loc, sec) 
        element.send_keys(inp_text) 


