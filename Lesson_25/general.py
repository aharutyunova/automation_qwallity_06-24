import logging 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

def getdriver():
    try:
        return webdriver.Chrome()
    except Exception as err:
        logging.error(err)

def geturl(driver, url):
    driver.get(url)

def locelement(driver, loc, sec = 10):
    try:
        elem = WebDriverWait(driver, sec).until(EC.presence_of_element_located(loc))
        logging.info("Element located")
        return elem
    except NoSuchElementException:
        logging.error("The element was not found on the page.")


def findandclick(driver, loc, sec=10):
    try:
        elem = WebDriverWait(driver, sec).until(EC.element_to_be_clickable(loc))
        elem.click()
        logging.info("Element clicked")
    except NoSuchElementException:
        logging.error("The element was not found on the page.")

def findandinput(driver, loc, inputtext, sec=10):
    try:
        input_field = WebDriverWait(driver, sec).until(EC.presence_of_element_located(loc))
        input_field.send_keys(inputtext)
        logging.info("Input field located and text was filled")
    except NoSuchElementException:
        logging.error("The element was not found on the page or something wrong with input")
            
def swithtoalert(driver):
    try:
        alert = driver.switch_to.alert
        logging.info("Alert swithched and text has been got")
        logging.info(alert.text)
        alert.accept()
    except NoAlertPresentException:
        logging.error("No alert was present.")

def assertion(expected, actual):
    try:
        assert expected == actual, f"Expected value '{expected}' but got '{actual}'"
        logging.info("Assertion passes, element is hidden")
    except AssertionError as err:
        logging.error(err)

def scrolluntilelement(driver, loc, sec = 10):
    try:
        element = WebDriverWait(driver, sec).until(EC.presence_of_element_located(loc))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        logging.info("Scrolled till the element")
        return element
    except NoSuchElementException as err:
        logging.error(err)
    

def hoveronandselectoption(driver, loc, element):
    try:
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        logging.info("Hovered on element")
        option_to_click = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
        actions.move_to_element(option_to_click).click().perform()
        logging.info("Hovered on element and selected an option")
    except Exception:
        logging.error("Something get wrong with hovering and getting an option")

def newtab(driver):
    try:
        original_window = driver.current_window_handle
        driver.execute_script("window.open('');")
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in driver.window_handles if window != original_window][0]
        driver.switch_to.window(new_window)
        logging.info("New tab is created and navigated")
        return original_window
    except Exception:
        logging.error("Something wrong with opening new tab")

def closealltabs(driver):
    try:
            for tab in driver.window_handles:
                driver.switch_to.window(tab)
                driver.close()
            logging.info("All tabs are closed")
    except Exception:
        logging.error("Something wrong with tab closing")
