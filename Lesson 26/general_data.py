from selenium import webdriver # Import the main Selenium WebDriver module for browser automation
from selenium.webdriver.support.ui import WebDriverWait # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC # Import expected_conditions for explicit waits


def get_driver(): # This function initializes the Chrome driver.
    try:
        return webdriver.Chrome()
    except Exception as e:
        raise Exception(e)


def find_element_ui(driver, loc, sec=10): # This function finds a single element in the UI and waits until it's visible.
    element = WebDriverWait(driver, sec).until(EC.visibility_of_element_located(loc))
    return element


def find_elements(driver, loc, sec=10): # This function finds multiple elements in the UI and waits until any of them are visible.
    elements = WebDriverWait(driver, sec).until(EC.visibility_of_any_elements_located(loc))
    return elements


def find_element_dom(driver, loc, sec=10): # This function finds a single element in the DOM and waits until it's present.
    element= WebDriverWait(driver, sec).until(EC.presence_of_element_located(loc))
    return element


def find_and_click(driver, loc, sec=10): # This function finds an element and waits until it's clickable, then clicks it.
    element = WebDriverWait(driver, sec).until(EC.element_to_be_clickable(loc))
    element.click()


def find_and_send_keys(driver, loc, input_text, sec=10): # This function finds an element, waits until it's clickable, then sends keys to it.
    element = WebDriverWait(driver, sec).until(EC.element_to_be_clickable(loc))
    element.send_keys(input_text)


def fill_and_click(driver, loc, input_text, sec=10): # This function finds an element, waits until it's clickable, sends keys to it, and then clicks it.
    element = WebDriverWait(driver, sec).until(EC.element_to_be_clickable(loc))
    element.click()
