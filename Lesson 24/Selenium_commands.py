from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()
driver = webdriver.Chrome()

driver.get("http://www.uitestingplayground.com/")
driver.maximize_window()
hidden_elements_count = []

# Task 1: Visibility Section
driver.find_element(By.LINK_TEXT, "Visibility").click()
hide_button = driver.find_element(By.ID, "hideButton")
hide_button.click()

zero_width = driver.find_elements(By.XPATH, "//*[@id='zeroWidthButton']")
hidden_elements_count.append("Zero Width")
overlapped = driver.find_element(By.XPATH, "//*[@id='hidingLayer']")
hidden_elements_count.append("Overlapped")
opacity_zero = driver.find_element(By.XPATH, "//*[@id='transparentButton']")
hidden_elements_count.append("Opacity 0")
visibility_hidden = driver.find_element(By.XPATH, "//*[@id='invisibleButton']")
hidden_elements_count.append("Visibility Hidden")
display_none = driver.find_element(By.XPATH, "//*[@id='notdisplayedButton']")
hidden_elements_count.append("Display None")
offscreen = driver.find_element(By.XPATH, "//*[@id='offscreenButton']")
hidden_elements_count.append("Offscreen")

driver.get("http://www.uitestingplayground.com/")
logger.info(f"Number of hidden elements: {len(hidden_elements_count)}")

# Task 2: Progress Bar Section
driver.find_element(By.LINK_TEXT, "Progress Bar").click()
start_button = driver.find_element(By.ID, "startButton")
start_button.click()
logger.info("Start button is clicked")
time.sleep(3)

stop_button = driver.find_element(By.ID, "stopButton")
stop_button.click()

progress_bar = driver.find_element(By.ID, "progressBar")
duration = progress_bar.get_attribute("aria-valuenow")

driver.get("http://www.uitestingplayground.com/")
logger.info("Stop button is clicked")
logger.info(f"Duration: {duration}")

# Task 3: Text Input Section
driver.find_element(By.LINK_TEXT, "Text Input").click()
text_field = driver.find_element(By.ID, "newButtonName")
text_field.send_keys("Test Button")

update_button = driver.find_element(By.ID, "updatingButton")
update_button.click()

button_text = update_button.text
if button_text == "Test Button":
    logger.info("Button text matches the entered text.")
else:
    logger.info("Button text does not match the entered text.")

driver.quit()
