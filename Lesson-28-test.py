from Helpers.basic_page import BasicHelper
from Helpers import logging_config
from Pages.main_login_page import MainLoginPage
from Test import test_data
from Test import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()  # Ensure the path to the ChromeDriver is correctly set
    logging_config.configure_logging()
    bh = BasicHelper(driver)
    main_lgn_page = MainLoginPage(driver)

    try:
        bh.open_url(config.url)
        main_lgn_page.fill_and_submit_login_form(test_data.email, test_data.code)
        logging.info("Successfully logged in!")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test is complete")
        driver.quit()
        logging.info("Closed all opened tabs")


if __name__ == '__main__':
    test()

    # Mariam jan, try keep files by folders, if you can't push it to github send it be with zip folder. Soluton is correct