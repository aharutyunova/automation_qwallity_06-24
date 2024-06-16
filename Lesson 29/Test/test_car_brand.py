
import pytest
import logging
from Helpers.basic_page import BasicHelper
from Pages.auto_am_page import Brands_Page
from selenium import webdriver
import config_data 


def test_search_car(driver):
    auto_page = Brands_Page(driver)
    logging.info("Starting test_search_car")
    auto_page.open_base_url(config_data.url)
    auto_page.search_a_brand(config_data.car_brand)
    results = auto_page.get_results_count()
    assert len(results) > 0, f"No results found for {config_data.car_brand}"
    logging.info(f"Found {len(results)} results for {config_data.car_brand}")
    logging.info("Test completed")


#  Anna - you had issue in conftest.py, with log_test_start_and_end method. You used logger there, but you didn't import it.
# I fixed it for you. Please, check it out.
# Also conftest.py file should be out of the Test folder. It should be in the root of the project.
# No need to import conftest.py file in the test file. It will be automatically imported by pytest.
# With debug test is passing. In tun mode it is failing.
# Config_data.py also will be better keep in root folder
