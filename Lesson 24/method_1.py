from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def method_one():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    try:
        # Step 1: Navigate to the URL
        driver.get("http://www.uitestingplayground.com/")
        logging.info("Navigated to uitestingplayground.com")

        # Step 2: Go to Visibility and click the Hide button
        driver.find_element(By.LINK_TEXT, "Visibility").click()
        hide_button = driver.find_element(By.ID, 'hideButton')
        hide_button.click()
        logging.info("Clicked on the Hide button")

        # Check that all other buttons are hidden
        # Check if "Zero Width" button is hidden
        Zero_Width_button = driver.find_element(By.ID, "zeroWidthButton")
        button_class = Zero_Width_button.get_attribute("class")
        assert "zerowidth" in button_class.split(), "Zero Width Button is not hidden"
        logging.info("Zero Width Button is hidden")

        # Check if the "Overlapped" button is hidden
        overlapped_button = driver.find_element(By.ID, "overlappedButton")
        button_style = overlapped_button.value_of_css_property("position")
        if "absolute" in button_style:
            logging.info("Overlapped Button is hidden")
        else:
            logging.info("Overlapped Button is visible")

        # Check if "Opacity 0" button is hidden
        Opacity_0_button = driver.find_element(By.ID, "transparentButton")
        opacity = Opacity_0_button.value_of_css_property("opacity")
        assert opacity == "0", "Opacity 0 Button is not hidden"
        logging.info("Opacity 0 Button is hidden")

        # Check if "Visibility" button is hidden
        Visibility_button = driver.find_element(By.ID, "invisibleButton")
        visibility = Visibility_button.value_of_css_property("visibility")
        assert visibility == "hidden", "Visibility Button is not hidden"
        logging.info("Visibility Button is hidden")

        # Check if "Display None" button is hidden
        Display_None_button = driver.find_element(By.ID, "notdisplayedButton")
        display = Display_None_button.value_of_css_property("display")
        assert display == "none", "Display None Button is not hidden"
        logging.info("Display None Button is hidden")

        # Check if "Offscreen" button is hidden
        Offscreen_button = driver.find_element(By.ID, "offscreenButton")
        button_class = Offscreen_button.get_attribute("class")
        assert "offscreen" in button_class.split(), "Offscreen Button is not hidden"
        logging.info("Offscreen Button is hidden")

    except Exception as e:
        logging.error("Error occurred: %s", e)

    finally:
        # Close the browser
        driver.quit()