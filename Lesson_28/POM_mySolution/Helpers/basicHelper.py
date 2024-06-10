import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Basic_Helper:
    def __init__(self, driver):
        self.driver = driver

    def geturl(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info(f"Open url {url}")

    def locelement(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
        logging.info("Element located")
        return elem
    
    def getElementValue(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
        value = elem.get_attribute('value')
        logging.info("Element value get")
        return value
    
    def findandclick(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc))
        elem.click()
        logging.info("Element clicked")

    def findandinput(self, loc, inputtext, sec=10):
        input_field = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
        input_field.send_keys(inputtext)
        logging.info("Input field located and text was filled")