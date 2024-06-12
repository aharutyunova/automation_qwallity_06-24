import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Basic_Helper:
    def __init__(self, driver):
        self.driver = driver

    def geturl(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info(f"Open url {url}")

    def find_element(self, loc, sec=10):
        elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
        logging.info("Element located")
        return elem
    
    def find_elements(self, loc, sec=10):
        elements = WebDriverWait(self.driver, sec).until(
            EC.visibility_of_any_elements_located(loc))
        return elements


    def findandinput(self, loc, inputtext, sec=10):
        elem = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
        elem.send_keys(inputtext)
        elem.send_keys(Keys.ENTER)
        logging.info("Input field located and text was filled")