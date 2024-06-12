# Anna, my homework is a bit messy, the only correct thing is that I used the POM method :). But since I didn't have time to work on it, I decided to push it.



import logging.config
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from Helpers import logging_config
import logging


def test_search_kia(driver):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)
    logging_config.configure_logging()
    logging.info("Search result")

    home_page.load()
    home_page.search_for_brand("Kia")

    assert search_results_page.has_results(), "Search results should not be null."

    # Anna -generally pytest format is correct but there are some notes
    # 1 In pages locators don't keep undet def __init__ () should keep out of __init__ I changed
    # 2 No need to import driver manager in conftest.py file.
    # 3. Will be good to keep logging also in conftest.py file
    # 4.  result_locator = (By.CLASS_NAME, "search-result") this locator return no result