import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()


def initialize_driver():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    except Exception as e:
        logger.error(f"Error initializing driver: {str(e)}")
        raise


def close_driver(driver):
    try:
        driver.quit()
        logger.info("Driver and all opened tabs are closed")
    except Exception as e:
        logger.error(f"Error closing driver: {str(e)}")


def find_elements(driver, loc, sec=10):
    try:
        elements = WebDriverWait(driver, sec).until(
            EC.visibility_of_any_elements_located(loc)
        )
        return elements
    except Exception as e:
        logger.error(f"Error finding elements: {str(e)}")
        raise


def find_element_ui(driver, loc, sec=10):
    try:
        element = WebDriverWait(driver, sec).until(
            EC.visibility_of_element_located(loc)
        )
        return element
    except Exception as e:
        logger.error(f"Error finding element in UI: {str(e)}")
        raise


def find_element_dom(driver, loc, sec=10):
    try:
        element = WebDriverWait(driver, sec).until(
            EC.presence_of_element_located(loc)
        )
        return element
    except Exception as e:
        logger.error(f"Error finding element in DOM: {str(e)}")
        raise


def find_and_click(driver, loc, sec=10):
    try:
        element = WebDriverWait(driver, sec).until(
            EC.element_to_be_clickable(loc)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)
        return element
    except Exception as e:
        logger.error(f"Error finding and clicking element: {str(e)}")
        raise


def find_and_send_keys(driver, loc, input_text, sec=10):
    try:
        element = find_element_ui(driver, loc, sec)
        element.send_keys(input_text)
        return element
    except Exception as e:
        logger.error(f"Error finding element and sending keys: {str(e)}")
        raise