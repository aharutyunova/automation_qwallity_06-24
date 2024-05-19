from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def perform_test(driver):
    try:
        driver.maximize_window()
        # Navigate to python.org
        driver.get("https://www.python.org")

        # Search "bla bla" text
        search_field = driver.find_element(By.ID, "id-search-field")
        search_field.send_keys("bla bla")
        # Click on Go button
        go_button = driver.find_element(By.ID, "submit")
        go_button.click()

        # Check Result will be No results found
        time.sleep(2)
        no_results_text = driver.find_element(By.XPATH, "//p[contains(text(),"
                                              "'No results found.')]")
        if no_results_text:
            logging.info("Test passed: No results found.")
        else:
            logging.warning("Test warning: Results found.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        # Close driver
        driver.close()


# List of browsers to test
browsers = ['chrome', 'firefox']


for browser in browsers:
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()

    logging.info(f"Starting test on {browser}")
    perform_test(driver)
    logging.info(f"Finished test on {browser}")


"""
Step 1) Open browser
Step 2) Navigate to python.org
Step 3) Search "bla bla" text
Step 4) Click on Go button
Step 5) Close driver
Step 6 ) Check Result will be No results found. 


Technical solution
Do the following in all type of browsers(Chrome and Firefox). Make for loop for sequence.
Handle exceptions
Use Logging
"""