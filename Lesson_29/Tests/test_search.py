import time

from Lesson_29.Pages.home_page import HomePage
from selenium import webdriver
from Lesson_29.Helpers import logging_config
from Lesson_29.Helpers.base_page import BasePage
from Lesson_29 import config
from Lesson_29 import testdata
import logging


def test_kia():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bp = BasePage(driver)
    home_page = HomePage(driver)

    try:
        logging.info("Starting test cases")
        bp.open_url(config.url)

        logging.info("Testing auto.am page")
        time.sleep(5)
        home_page.enter_search_key(testdata.search_keyword)
        time.sleep(5)
        home_page.click_search_btn()
        logging.info("Testing search result")
        time.sleep(10)
        home_page.get_result()
        time.sleep(5)
        logging.info("All test cases are passed")

    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test is completed")
        driver.quit()
        logging.info("All opened tabs are closed")


if __name__ == '__main__':
    test_kia()
    print("This test case finished successfully!")
