from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


def open_url(driver, url):
    driver.maximize_window()
    logging.info("Browser window maximized")
    driver.get(url)
    logging.info(f"URL opened: {url}")


def find_elem_ui(driver, loc, sec=10):
    elem = WebDriverWait(driver, sec).until(
        EC.visibility_of_element_located(loc))
    return elem


def find_elements(driver, loc, sec=10):
    elements = WebDriverWait(driver, sec).until(
        EC.visibility_of_any_elements_located(loc))
    return elements


def find_elem_dom(driver, loc, sec=10):
    elem = WebDriverWait(driver, sec).until(
        EC.presence_of_element_located(loc))
    return elem


def find_and_click(driver, loc, sec=10):
    elem = WebDriverWait(driver, sec).until(
        EC.element_to_be_clickable(loc))
    elem.click()


def find_and_send_keys(driver, loc, inp_text, sec=10):
    elem = find_elem_ui(driver, loc, sec)
    elem.send_keys(inp_text)
