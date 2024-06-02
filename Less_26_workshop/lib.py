from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains


def move_to_element(loc, driver, timeout=10):
    actions = ActionChains(driver)
    el = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(loc))
    actions.move_to_element(el).perform()


def get_element(loc, driver, timeout=10):
    el = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(loc))
    return el


def get_elements(loc, driver, timeout=10):
    elements = driver.find_elements(*loc)
    return elements


def click_on_element(loc, driver, timeout=10):
    WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(loc)).click()


def input_text(loc, driver, text, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_elemget_element_textent_located(loc)).send_keys(text)
