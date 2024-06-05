
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def configure_logging():
    logging.basicConfig(
        filename='test_case.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')


configure_logging()
logging.info("Starting the test case")


driver = webdriver.Chrome()


driver.get("https://www.letskodeit.com/login")
# 10
email_field = driver.find_element(By.ID, "email")
email_field.send_keys('aaaaa@email.com')

password_field = driver.find_element(By.ID, "login-password")
password_field.send_keys('password')
logging.info("Entered password")

login_button = driver.find_element(By.ID, "login")
login_button.click()
logging.info("Clicked login button")


wait = WebDriverWait(driver, 10)
validation_message = wait.until(EC.visibility_of_element_located((By.ID, "incorrectdetails")))

# 11
message_text = validation_message.text
print(message_text)
logging.info(f"Validation message: {message_text}")
# 12
driver.execute_script("window.open('');")
logging.info("Opened a new tab")

driver.switch_to.window(driver.window_handles[1])
logging.info("Switched to the new tab")
# 13
driver.get("https://www.python.org/")
logging.info("Opened https://www.python.org/ in the new tab")

# 14
search_field = driver.find_element(By.ID, "id-search-field")
search_field.send_keys('Automation')
search_field.submit()
time.sleep(10)

all_windows = driver.window_handles
driver.switch_to.window(all_windows[0])
logging.info("Switched to the first page")

driver.quit()
logging.info("Test case ended and browser closed")

# Separate functions works, will discuss tomorrow group actions by functions and by pages