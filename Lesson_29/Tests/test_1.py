from Pages.search import SearchPage
import config
import testdata
import logging
import time

def test(driver):

    si = SearchPage(driver)
    si.geturl(config.base_url)
    brand = si.searchInput(testdata.car_name)
    assert brand.lower() == (testdata.car_name).lower(), logging.error("Search is failed")
    time.sleep(5)     
    result = si.searchresult()
    assert len(result) > 0, logging.error("No result")
    logging.info("Test passed")

# Ray jan generel concept is correct but there is some notes and the MOST IMPORTNAT
#  NEVER PUT ASSERT In try except block. In this case your test always will pass and never fail even assertion will fail

# Input field locator should be   search_input_loc = (By.XPATH, "//input[@id='searchInp']")
# As result is return list of elements you should assert len(result)
# After input car model name a bit time needed, otherwise system can't click enter and ddl of cars not disappeared