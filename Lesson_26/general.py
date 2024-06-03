from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    try:
        return webdriver.Chrome()
    except Exception as e:
        raise Exception(e)


def find_elem_ui(driver, loc, sec=10):
    elem = WebDriverWait(driver, sec).until(EC.visibility_of_element_located(loc))
    return elem


def find_elements(driver, loc, sec=10):
    elements = WebDriverWait(driver, sec).until(EC.visibility_of_any_elements_located(loc))
    return elements


def find_elem_dom(driver, loc, sec=10):
    elem = WebDriverWait(driver, sec).until(EC.presence_of_element_located(loc))
    return elem


def find_and_click(driver, loc, sec=10):
    elem = WebDriverWait(driver, sec).until(EC.element_to_be_clickable(loc))
    elem.click()


def find_and_send_keys(driver, loc, input_text, sec=10):
    elem = WebDriverWait(driver, sec).until(EC.element_to_be_clickable(loc))
    elem.send_keys(input_text)


def fill_and_click(driver, loc, input_text, sec=10):
    elem = WebDriverWait(driver, sec).until(EC.element_to_be_clickable(loc))
    elem.click()


def write_in_file(text):
    with open('live_coding.txt', 'a+') as f:
        f.write(text + '\n')
