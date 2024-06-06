from Workshop_28.Helpers.basic_page import BasicHelper
from Workshop_28.Helpers import logging_config
from Workshop_28.Pages.main_login_page import Main_Login_page
# from Workshop_28.Pages.python_org import Python_Org
# from Workshop_28.Pages.sign_in import Sign_In_Page
from Workshop_28 import test_data
from Workshop_28 import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bh = BasicHelper(driver)
    main_lgn_page = Main_Login_page(driver)

    try:
        bh.open_url(config.url)
        main_lgn_page.fill_and_submit_login_form(test_data.email, test_data.code)
        logging.info("Successfuly loged in!")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test is Pass")
        driver.quit()
        logging.info("Closed all opened tabs")

    if __name__ == '__main__':
        test()
