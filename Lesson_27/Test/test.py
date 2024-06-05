from Helpers.basic_page import Basic_Helper
from Helpers import logging_config
from Pages.result import Result_Page
from Pages.practise import Practise_Page
from Pages.python_org import Python_Org
from Pages.sign_in import Sign_In_Page
import testdata
import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bp = Basic_Helper(driver)
    practise_page = Practise_Page(driver)
    result = Result_Page(driver)
    python_org_page = Python_Org(driver)
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
    test()
    print("This test case finished, but not successfully!:D")



# Ann jan finally managed to solve this task, I do not know how but it works :D
# and hope the solution is  correct :D
# the only thing that is not working is as always the banner does not allow system to find and click
# on sign in button

#  Anna - the structure is correct and for first page object model structure really very good!!!
# Sign in is not clickable in your example you call sign_in method from sign_in_page , in that method you don't click on sign_in link
# Also you have sign_in method in practise page, where you call click on the sign in link, if you call sign in method from practise page, everything will work