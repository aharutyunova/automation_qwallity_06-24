from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def url(driver, url):
    """
    Open the specified URL and maximize the browser window.

    :param driver: WebDriver instance to control the browser
    :param url: URL to open in the browser
    """
    driver.maximize_window()
    logging.info("Browser window maximized")
    driver.get(url)
    logging.info(f"URL opened: {url}")

def wait_for_element_visibility(driver, locator, timeout=10):
    """
    Wait for an element to be visible on the UI.

    :param driver: WebDriver instance to control the browser
    :param locator: Locator tuple to find the element (e.g., (By.ID, 'element_id'))
    :param timeout: Maximum time to wait for the element (default is 10 seconds)
    :return: WebElement once it becomes visible
    """
    logging.info(f"Waiting for element visibility: {locator}")
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator))
    logging.info(f"Element visible: {locator}")
    return element

def wait_for_elements_visibility(driver, locator, timeout=10):
    """
    Wait for multiple elements to be visible on the UI.

    :param driver: WebDriver instance to control the browser
    :param locator: Locator tuple to find the elements (e.g., (By.CLASS_NAME, 'element_class'))
    :param timeout: Maximum time to wait for the elements (default is 10 seconds)
    :return: List of WebElements once they become visible
    """
    logging.info(f"Waiting for elements visibility: {locator}")
    elements = WebDriverWait(driver, timeout).until(
        EC.visibility_of_any_elements_located(locator))
    logging.info(f"Elements visible: {locator}")
    return elements

def wait_for_element_presence(driver, locator, timeout=10):
    """
    Wait for an element to be present in the DOM.

    :param driver: WebDriver instance to control the browser
    :param locator: Locator tuple to find the element (e.g., (By.XPATH, '//element_xpath'))
    :param timeout: Maximum time to wait for the element (default is 10 seconds)
    :return: WebElement once it is present in the DOM
    """
    logging.info(f"Waiting for element presence in DOM: {locator}")
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator))
    logging.info(f"Element present in DOM: {locator}")
    return element

def wait_for_element_and_click(driver, locator, timeout=10):
    """
    Wait for an element to be clickable and then click it.

    :param driver: WebDriver instance to control the browser
    :param locator: Locator tuple to find the element (e.g., (By.NAME, 'element_name'))
    :param timeout: Maximum time to wait for the element to be clickable (default is 10 seconds)
    """
    logging.info(f"Waiting for element to be clickable: {locator}")
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator))
    element.click()
    logging.info(f"Element clicked: {locator}")

def wait_for_element_and_send_keys(driver, locator, input_text, timeout=10):
    """
    Wait for an element to be visible and send keys to it.

    :param driver: WebDriver instance to control the browser
    :param locator: Locator tuple to find the element (e.g., (By.TAG_NAME, 'element_tag'))
    :param input_text: Text to send to the element
    :param timeout: Maximum time to wait for the element (default is 10 seconds)
    """
    logging.info(f"Waiting for element to send keys: {locator}")
    element = wait_for_element_visibility(driver, locator, timeout)
    element.send_keys(input_text)
    logging.info(f"Keys sent to element: {locator} - Input: {input_text}")
