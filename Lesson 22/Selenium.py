from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

logging.basicConfig(level=logging.INFO,
                    filename='logs.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
driver = webdriver
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
        assert expected_result in body_text, f"Expected '{expected_result}' " \
                                             f"to be in the search results, but found: {body_text}"
        logger.info(f"Search result as expected: {expected_result}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    finally:
        driver.quit()
        print("Test is finished")
        logger.info("Closed browser and ended session.")

logger.info("Test is finished.")
