import pytest 
from selenium import webdriver
import logging


def configure_logging():
    logging.basicConfig(
        filename='test_case.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


@pytest.fixture()
def drive()
    dr = webdriver.Chrome
    yield dr
    dr.quit()

def test_search_kia_results_not_null(driver)
    auto_page = AutoAmPage(driver)
    auto_page.go_to_auto_am()
    auto_page.search_for_brand('Kia')
    results = auto_page.get_search_results()
    assert results is not None, "Search results for Kia are null"

    class AutoAmPage:
      def __init__(self, driver):
        self.driver = driver
        self.url = "https://auto.am"

      def go_to_auto_am(self):
        self.driver.get(self.url)

    def search_for_brand(self, brand):
        search_box = self.driver.find_element_by_id("main-search-input")
        search_box.clear()
        search_box.send_keys(brand)
        search_box.submit()

    def get_search_results(self)
       pass


# Mariam jan general methods and actions are correct, but it doesn't work because everything in the same file