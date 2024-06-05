from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    try:
        return webdriver.Chrome()
    except Exception as error:
        raise Exception(error)


def find_element_ui(driver, locator, sec=10):
    element = WebDriverWait(driver, sec).until(
        EC.visibility_of_element_located(locator))
    return element


def find_elements(driver, locator, sec=10):
    elements = WebDriverWait(driver, sec).until(
        EC.visibility_of_any_elements_located(locator))
    return elements


def find_element_dom(driver, locator, sec=10):
    element = WebDriverWait(driver, sec).until(
        EC.presence_of_element_located(locator))
    return element


def find_and_click(driver, locator, sec=10):
    element = WebDriverWait(driver, sec).until(
        EC.element_to_be_clickable(locator))
    element.click()


def find_and_send_keys(driver, locator, input_text, sec=10):
    element = find_element_ui(driver, locator, sec)
    element.send_keys(input_text)
