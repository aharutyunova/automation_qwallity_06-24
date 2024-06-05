import sys
import os

# Ensure the root directory is in the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Helpers.basic_page import BasicHelper
from Helpers import logging_config
from Pages.practice_page import Practice_Page
from Pages.python_page import Python_Page
from Pages.login_page import Login_Page
import test_data
import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bh = BasicHelper(driver)
    pr_page = Practice_Page(driver)
    py_page = Python_Page(driver)
    login_page = Login_Page(driver)

    try:
        bh.open_url(config.url)
        pr_page.click_alert_popup()
        pr_page.hide_element_and_check()
        pr_page.scroll_and_click_mouse_hover()
        pr_page.get_footer_text()
        pr_page.click_sign_in()
        login_page.fill_and_submit_login_form(test_data.email_data, test_data.pass_data)
        login_page.validation_message()
        py_page.open_new_tab_and_search(config.new_tab_url, test_data.search_data)
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test is Pass")
        driver.quit()
        logging.info("Closed all opened tabs")


if __name__ == '__main__':
    test()
