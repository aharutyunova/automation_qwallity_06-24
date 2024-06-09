from Helpers.basic_page import Basic_Helper
from Helpers import logging_config
from Pages.result import Result_Page
from Pages.practise import Practise_Page
from Pages.python_org import Python_Org
from Pages import testdata
from Pages import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bp = Basic_Helper(driver)
    practise_page = Practise_Page(driver)
    result = Result_Page(driver)
    python_org_page = Python_Org(driver)
    validation_text = Sign_In_Page(driver).validation_msg_loc
    sign_in_page = Sign_In_Page(driver)
    try:
        logging.info("Starting test cases")
        bp.open_url(config.url)

        logging.info("Testing Practise Page")
        practise_page.save_alert_text()
        practise_page.hide_element_check()
        practise_page.mouse_hover_check()
        practise_page.footer_text()

        logging.info("Testing Sign In Page")
        practise_page.sign_in(testdata.email_data, testdata.password_data)
        sign_in_page.sign_in()

        logging.info("Testing Python Org Page")
        python_org_page.python_search()

        logging.info("All test cases passed")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        if driver:
            bp.close_driver()
            logging.info("Driver closed")


if __name__ == '__main__': 
    print("This test case finished")