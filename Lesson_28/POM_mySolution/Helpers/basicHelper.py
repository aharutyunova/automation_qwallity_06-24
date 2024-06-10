
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
            
    def swithtoalert(self):
        alert = self.driver.switch_to.alert
        logging.info("Alert swithched and text has been got")
        logging.info(alert.text)
        alert.accept()

    def assertion(expected, actual):
        assert expected == actual, f"Expected value '{expected}' but got '{actual}'"
        logging.info("Assertion passes, element is hidden")

    def scrolluntilelement(self, loc, sec = 10):
        element = WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        logging.info("Scrolled till the element")
        return element

    def hoveronandselectoption(self, loc, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        logging.info("Hovered on element")
        option_to_click = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        actions.move_to_element(option_to_click).click().perform()
        logging.info("Hovered on element and selected an option")

    def newtab(self):
        original_window = self.driver.current_window_handle
        self.driver.execute_script("window.open('');")
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        logging.info("New tab is created and navigated")
        return original_window
        
    def closealltabs(self):
        for tab in self.driver.window_handles:
            self.driver.switch_to.window(tab)
            self.driver.close()
            logging.info("All tabs are closed")
