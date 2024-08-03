from Pages.main_page import AutoPage
import logging
import config
from Helpers import logging_config
import time

logging_config.configure_logging()


def test_case(driver):
    main_page = AutoPage(driver)
    try:
        logging.info("Starting test case!")
        main_page.open_url(config.url)
        main_page.search_car(config.car_brand)
        time.sleep(1)
        results = main_page.get_result()
        assert len(results) > 0, "No results found for Kia"
        logging.info(f"Found {len(results)} results for {config.car_brand}")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test completed")

