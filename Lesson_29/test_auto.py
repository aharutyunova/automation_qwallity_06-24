# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pages.auto_page import Auto_Page
import logging
import config


def test_search_car(driver):
    auto_page = Auto_Page(driver)
    try:
        logging.info("Starting test_search_car")
        auto_page.open_url(config.url)
        auto_page.search_car(config.car_brand)
        results = auto_page.get_results_count()
        assert len(results) > 0, "No results found for Ford"
        logging.info(f"Found {len(results)} results for {config.car_brand}")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test completed")
