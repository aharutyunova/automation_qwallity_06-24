# Anna, my homework is a bit messy, the only correct thing is that I used the POM method :). But since I didn't have time to work on it, I decided to push it.



import logging.config
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from Lesson_29.Helpers import logging_config
import logging


def test_search_kia(driver):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)
    logging_config.configure_logging()
    logging.info("Search result")

    home_page.load()
    home_page.search_for_brand("Kia")

    assert search_results_page.has_results(), "Search results should not be null."