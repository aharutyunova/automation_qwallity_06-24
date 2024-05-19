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


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

browsers = ["chrome", "firefox","edge"]

for browser in browsers:
    try:
        # Initialize the driver
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "edge":
            driver = webdriver.Edge()
        else:
            logging.error(f"Browser {browser} is not supported.")
            continue

        # Step 1) Maximize the window
        driver.maximize_window()
        logging.info(f"Opened {browser} browser.")

        # Step 2) Navigate to python.org
        driver.get("https://www.python.org")
        logging.info("Navigated to python.org")

        # Step 3) Find search bar and enter "bla bla"
        search_bar = driver.find_element(By.ID, "id-search-field")
        search_bar.send_keys("bla bla")
        logging.info('Entered "bla bla" in the search bar.')

        # Step 4) Click the search button
        search_button = driver.find_element(By.ID, "submit")
        search_button.click()
        logging.info("Clicked the search button.")

        # Wait for results to load
        time.sleep(3)

        # Step 5) Check if "No results found." is displayed
        try:
            no_result_text = driver.find_element(By.XPATH, "//*[@id='content']/div/section/form/ul/p").text
            assert no_result_text == "No results found."
            logging.info('Verified "No results found." text is displayed.')
        except AssertionError:
            logging.error('"No results found." text is not displayed.')
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    except Exception as e:
        logging.error(f"An error occurred with {browser}: {str(e)}")
    finally:
        # Step 6) Close driver
        driver.close()
        logging.info(f"Closed {browser} browser.")

if "No results found." == no_result_text:
    logging.info("Test is successfully completed.")
else:
    logging.info("Ooops! Test is failed.")


