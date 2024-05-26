"""
1. Navigate by the following URL:  https://www.letskodeit.com/practice  
2. Find effective XPaths  for the elements that are highlighted in the screenshot below.
3. Print how many elements you found in total.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

browsers = ["chrome", "firefox", "edge"]

total_elements_found = 0

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

        # Maximize the window
        driver.maximize_window()
        logging.info(f"Opened {browser} browser.")

        # Navigate to the website
        driver.get("https://www.letskodeit.com/practice")
        logging.info("Navigated to letskodeit.com")

        # List of XPath expressions for the elements
        xpaths = [
            '//*[@id="radio-btn-example"]/fieldset/label[2]',
            '//*[@id="checkbox-example-div"]/fieldset/label[3]',
            '//*[@id="multiple-select-example"]/option[2]',
            '//*[@id="multiple-select-example"]/option[3]',
            '//*[@id="show-textbox"]',
            '//*[@id="displayed-text"]',
            '//*[@id="name"]',
            '//*[@id="mouse-hover-example-div"]/div[1]/fieldset/legend'
        ]

        # Find elements using the specified XPaths
        elements_found = 0
        for xpath in xpaths:
            try:
                element = driver.find_element(By.XPATH, xpath)
                elements_found += 1
                logging.info(f'Element found for XPath: {xpath}')
            except Exception as e:
                logging.error(f'Element not found for XPath: {xpath}. Error: {str(e)}')

        # Add the found elements count to the total
        total_elements_found += elements_found

        # Close the browser
        driver.quit()

    except Exception as e:
        logging.error(f"Error with {browser} browser: {str(e)}")

# Print the total number of elements found
print(f"Total number of elements found: {total_elements_found}")
