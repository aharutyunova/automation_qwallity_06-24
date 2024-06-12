from Helpers.logging_ import logging_
from pages.search import SearchPage
import config
import testdata
import logging
import time


def test(driver):

    logging_()
    si = SearchPage(driver)
    si.geturl(config.base_url)
    si.searchInput(testdata.car_name)
    #assert brand == testdata.car_name, logging.error("Search is failed")
    
    time.sleep(1)   
    result = si.searchresult()
    assert len(result) > 0, logging.error("No result")


# Ray jan generel concept is correct but there is some notes and the MOST IMPORTNAT
#  NEVER PUT ASSERT In try except block. In this case your test always will pass and never fail even assertion will fail

# Input field locator should be   search_input_loc = (By.XPATH, "//input[@id='searchInp']")
# As result is return list of elements you should assert len(result)
# After input car model name a bit time needed, otherwise system can't click enter and ddl of cars not disappeared