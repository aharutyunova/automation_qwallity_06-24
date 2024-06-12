from Helpers.logging_ import logging_
from Pages.search import SearchPage
import config
import testdata
import logging
import time


def test(driver):
    try:
        logging_()
        si = SearchPage(driver)
        si.geturl(config.base_url)
        brand = si.searchInput(testdata.car_name)
        #assert brand == testdata.car_name, logging.error("Search is failed")
        time.sleep(1)   
        result = si.searchresult()
        assert result > 0, logging.error("No result")
    except Exception as err:
        logging.error(f"Search has got an error: {err}")

