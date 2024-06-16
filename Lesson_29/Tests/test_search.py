import time
from Lesson_29.Pages.home_page import HomePage
from selenium import webdriver
from Lesson_29.Helpers import logging_config
from Lesson_29.Helpers.base_page import BasePage
from Lesson_29 import config
from Lesson_29 import (testdata)
import logging


def test_kia():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bp = BasePage(driver)
    home_page = HomePage(driver)

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





# Anna - where is assertion in test case? :)
#  When use pytest no need to call function in the test case (line 42 in your solution) pytest will call all functions started with test
# Also no need to quit() driver in the test case, as you already do it in conftest.py file
# A lot of time.sleeps(), use time sleep in exceptional cases only, and 1-2 seconds, not 5-10
# Locators for input field and search button was incorrect, I changed them
# Don't put all test case in try except block, because it always will pass, instead use assertion for main condition
# If assertion will pass test also will pass, otherwise will fail

