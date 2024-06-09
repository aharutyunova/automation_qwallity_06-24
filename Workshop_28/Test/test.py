import sys
import os

# Ensure the root directory is in the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Helpers.basic_page import BasicHelper
from Helpers import logging_config
from Pages.main_login_page import Main_Login_Page
from Pages.home_page import Home_Page
from Pages.home_login_page import Home_Login_Page
from Pages.user_action_page import User_Action_Page
import test_data
import config
from selenium import webdriver
import logging


def test():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bh = BasicHelper(driver)
    main_lgn_page = Main_Login_Page(driver)
    hm_page = Home_Page(driver)
    hm_login_page = Home_Login_Page(driver)
    user_act_page = User_Action_Page(driver)

    try:
        bh.open_url(config.url)
        main_lgn_page.fill_and_submit_login_form(test_data.email, test_data.code)
        hm_page.click_login()
        logging.info("Login page opened")
        hm_login_page.fill_and_submit_second_login_form(test_data.username, test_data.password)
        logging.info("Home page opened")
        hm_page.click_user_action_btn()
        logging.info("User Action page opened")
        acc_balance = user_act_page.get_balance()
        logging.info(f"Balance is: {acc_balance}")
        user_act_page.add_ammoun_and_submit_checkout_btn(test_data.amount)
        new_acc_balance = user_act_page.get_balance()
        logging.info(f"New Account Balance is: {new_acc_balance}")
        logging.info("New balance is correct")
        assert ((int(acc_balance) + int(test_data.amount)) == int(new_acc_balance))
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test completed")
        driver.quit()
        logging.info("Closed all opened tabs")


if __name__ == '__main__':
    test()

# Anna Good job and good structure