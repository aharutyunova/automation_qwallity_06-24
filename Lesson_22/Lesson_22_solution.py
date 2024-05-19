import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    log_file_path = os.path.join(CURRENT_DIR, 'Lesson_22_log')

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log_file_path,
        filemode='w+',
        encoding='utf-8'
    )
except Exception as e:
    logging.error("Error setting up logging: %s", str(e))


browser_list = {1: "Chrome", 2: "Firefox", 3: "MicrosoftEdge"}


for browser in browser_list.values():
    try:
        driver = getattr(webdriver, browser, None)()
        if driver is None:
            logging.error(f"Browser '{browser}' is not supported")

        try:
            driver.maximize_window()
            driver.get("https://www.python.org")
            search = driver.find_element(By.ID, "id-search-field")
            button_go = driver.find_element(By.ID, "submit")
            search.send_keys("bla bla")
            button_go.click()
            logging.info(f"Test completed successfully on {browser}")
        except Exception as e:
            logging.error(
                f"An error occurred while performing actions on {browser}: {e}"
                )
        finally:
            driver.quit()
            logging.info(f"{browser} browser closed.")
    except Exception as e:
        logging.error(
            f"An error occurred while setting up {browser} browser: {e}"
            )
