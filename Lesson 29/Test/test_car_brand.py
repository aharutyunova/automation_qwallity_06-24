
import pytest
import logging

from Helpers.basic_page import BasicHelper
from Pages.auto_am_page import Brands_Page
from selenium import webdriver
import config_data 
import conftest


def test_search_car(driver):
    auto_page = Brands_Page(driver)
    logging.info("Starting test_search_car")
    auto_page.open_base_url(config_data.url)
    auto_page.search_a_brand(config_data.car_brand)
    results = auto_page.get_results_count()
    assert len(results) > 0, f"No results found for {config_data.car_brand}"
    logging.info(f"Found {len(results)} results for {config_data.car_brand}")
    logging.info("Test completed")

