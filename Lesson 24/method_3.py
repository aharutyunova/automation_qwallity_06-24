from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def method_three():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    try:

        # Step 1: Navigate to the URL
        driver.get("http://www.uitestingplayground.com/")
        logging.info("Navigated to uitestingplayground.com")

        # Step 2: Go to Text Input
        driver.find_element(By.LINK_TEXT, "Text Input").click()
        input_field = driver.find_element(By.ID, "newButtonName")
        input_text = "Test Text"
        input_field.send_keys(input_text)
        update_button = driver.find_element(By.ID, "updatingButton")
        update_button.click()
        # Check if the button text is the same as the entered text
        button_text = update_button.text
        logging.info("Button text matches entered text: %s", button_text == input_text)

    except Exception as e:
        logging.error("Error occurred: %s", e)

    finally:
        # Close the browser
        driver.quit()