from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


def open_url(driver, url):
    driver.maximize_window()
    logging.info("Browser window maximized")
    driver.get(url)
    logging.info(f"URL opened: {url}")


def open_new_tab_and_switch_to_it(driver):
    driver.execute_script("window.open('');")
    logging.info("New tab opened")
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])


def go_to_the_first_page(driver):
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[0])
    logging.info("Getting back to the first tab")


def find_elem_ui(driver, loc, sec=20):
    try:
        logging.info(f"Waiting for element visibility: {loc}")
        elem = WebDriverWait(driver, sec).until(
            EC.visibility_of_element_located(loc))
        logging.info(f"Element visible: {loc}")
        return elem
    except Exception as e:
        logging.error(f"Error finding UI element {loc}: {e}")


def find_elements(driver, loc, sec=10):
    logging.info(f"Waiting for elements visibility: {loc}")
    elements = WebDriverWait(driver, sec).until(
        EC.visibility_of_any_elements_located(loc))
    logging.info(f"Elements visible: {loc}")
    return elements


def find_elem_dom(driver, loc, sec=10):
    logging.info(f"Waiting for element presence in DOM: {loc}")
    elem = WebDriverWait(driver, sec).until(
        EC.presence_of_element_located(loc))
    logging.info(f"Element present in DOM: {loc}")
    return elem


def find_and_click(driver, loc, sec=10):
    logging.info(f"Waiting for element to be clickable: {loc}")
    elem = WebDriverWait(driver, sec).until(
        EC.element_to_be_clickable(loc))
    elem.click()
    logging.info(f"Element clicked: {loc}")


def find_and_send_keys(driver, loc, inp_text, sec=10):
    logging.info(f"Waiting for element to send keys: {loc}")
    elem = find_elem_ui(driver, loc, sec)
    elem.send_keys(inp_text)
    logging.info(f"Keys sent to element: {loc} - Input: {inp_text}")
