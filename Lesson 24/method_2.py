from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
                    
def method_two():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    try:
        # Step 1: Navigate to the URL
        driver.get("http://www.uitestingplayground.com/")
        logging.info("Navigated to uitestingplayground.com")

        # Step 2: Go to Progress Bar
        progress_bar_link = driver.find_element(By.LINK_TEXT, "Progress Bar")
        progress_bar_link.click()
        start_button = driver.find_element(By.ID, "startButton")
        start_button.click()
        time.sleep(6)  # Wait for some time to let the progress bar fill
        stop_button = driver.find_element(By.ID, "stopButton")
        stop_button.click()
        progress_bar = driver.find_element(By.ID, "progressBar")
        progress_percentage = int(progress_bar.get_attribute("aria-valuenow"))
        logging.info("Duration: %s%%", progress_percentage)

    except Exception as e:
        logging.error("Error occurred while locating Progress Bar link: %s", e)

    finally:
        # Close the browser
        driver.quit()
