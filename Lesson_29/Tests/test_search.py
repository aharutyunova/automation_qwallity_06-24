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
        home_page.click_search_btn()
        logging.info("Testing search result")
        home_page.get_result()
        logging.info("All test cases are passed")

    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test is completed")
        driver.quit()
        logging.info("All opened tabs are closed")


if __name__ == '__main__':
    test_kia()
    print("This test case finished, but not successfully!:D")











'''

class TestSearch:
    def test_search_kia(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.enter_search_term("Kia")
        home_page.click_search_button()

        results_page = SearchResultsPage(self.driver)
        assert results_page.results_exist(), "No results found for 'Kia'"


import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pytest_auto_am.conftest import driver


def enter_search_key(driver):
        driver.get("https://auto.am")

    search_inpt = driver.find_element(By.XPATH, '//*[@id="searchInp-small"]')
    search_box.clear()

    # Enter 'Mazda' into the search box
    search_box.send_keys("Mazda")

    # Wait for 5 seconds to ensure the search results load
    time.sleep(5)

    # Submit the search by pressing the Enter key
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load using WebDriverWait
    wait = WebDriverWait(driver, 5)
    try:
        results = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search-result"]')))
    except TimeoutException:
        print("TimeoutException: No elements found with class name 'car-list-item'")
        raise

    # Print the number of results found
    print(f"Found {len(results)} results.")

    # Check that results are not "Null"
    assert len(results) > 0, "No results found for 'Mazda'"

'''
