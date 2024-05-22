from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def perform_test(driver):
    try:
        driver.maximize_window()
        driver.get("https://www.letskodeit.com/practice")

        # XPaths for the specified elements
        elements_xpath = {
            "rbt": "//input[@id='benzradio']",
            "ch_box": "//input[@id='hondacheck']",
            "switch_tab": "//a[@id='opentab']",
            "multi_sel_or": "//option[@value='orange']",
            "multi_sel_pe": "//option[@value='peach']",
            "eldisp_bt": "//input[@id='show-textbox']",
            "eldisp_inp": "//input[@id='displayed-text']",
            "switchto_input": "//input[@name='enter-name']",
            "mouse_hover": "//legend[contains(text(),'Mouse Hover Example')]",
            "web_table_course": "//td[contains(text(),'Python Programming Language')]"
        }

        total_elements = 0

        for description, xpath in elements_xpath.items():
            elements = driver.find_elements(By.XPATH, xpath)
            element_count = len(elements)
            total_elements += element_count
            logging.info(f"{description}: {element_count} element(s) found.")

        logging.info(f"Total elements found: {total_elements}")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        driver.close()


# List of browsers to test
browser_list = ['chrome']

for browser in browser_list:
    try:
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()

        logging.info(f"Starting test on {browser}")
        perform_test(driver)
        logging.info(f"Finished test on {browser}")

    except Exception as e:
        logging.error(f"Error with {browser} browser: {e}")

# An jan very good, xpaths are optimal and the way of count elements also good organized
# Keep it up!!!