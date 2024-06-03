from Helpers.basic_page import Basic_Helper
from Helpers import logging_config
from Pages.main import Main_Page
from Pages.result import Result_Page
import testdata
import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bp = Basic_Helper(driver)
    main_page = Main_Page(driver)
    result_page = Result_Page(driver)

    bp.open_url(config.url)
    main_page.search_word(testdata.search_word)
    result_number = result_page.get_result()
    assert result_number > 0, logging.error("No result is found")
    logging.info("Result is found")
    field_value = result_page.get_search_input_value()
    assert field_value == testdata.search_word, logging.error(f"Field value {field_value} doesn't equal to search word {testdata.search_word}")
    logging.info(f"Field value {field_value} equal to search word {testdata.search_word}")
    logging.info("Test is Pass")
    driver.quit()


if __name__ == '__main__':
    test()
