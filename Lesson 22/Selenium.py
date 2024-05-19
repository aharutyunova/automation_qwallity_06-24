from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

browsers = ["chrome", "firefox"]

url = "https://www.python.org"
search_text = "bla bla"
search_box_name = "q"
expected_result = "No results found."

for browser in browsers:
    try:
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        logger.info(f"Opened {browser} browser.")

        driver.get(url)
        logger.info(f"Navigated to {url}")

        search_box = driver.find_element(By.NAME, search_box_name)
        search_box.send_keys(search_text)
        logger.info(f"Entered search text: {search_text}")

        search_box.send_keys(Keys.RETURN)
        logger.info("Clicked on Go button.")

        time.sleep(3)

        body_text = driver.find_element(By.TAG_NAME, "body").text
        if expected_result in body_text:
            logger.info(f"Search result as expected: {expected_result}")
        else:
            logger.warning(f"Search result not as expected. Found: {body_text}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    finally:
        driver.quit()
        print("Test is finished")
        logger.info("Closed browser and ended session.")

logger.info("Test is finished.")

# Anna - good solution, everything is correct, only fo rlog file use .log extension 
# And you could assert body_text ==  expected_result not check with if and else
