from Workshop_28.Helpers.basic_page import BasicHelper
from Workshop_28.Helpers import logging_config
from Workshop_28.Pages.main_login_page import MainLoginPage
from Workshop_28.Pages.home_page import HomePage
from Workshop_28.Pages.home_login_page import HomeLoginPage
from Workshop_28.Pages.user_action_page import UserActionPage
from Workshop_28 import test_data
from Workshop_28 import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()  # Ensure the path to the ChromeDriver is correctly set
    logging_config.configure_logging()
    bh = BasicHelper(driver)
    main_lgn_page = MainLoginPage(driver)
    home_page = HomePage(driver)
    home_lgn_page = HomeLoginPage(driver)
    user_action_page = UserActionPage(driver)

    try:
        bh.open_url(config.url)
        main_lgn_page.fill_and_submit_login_form(test_data.email, test_data.code)
        logging.info("Successfully logged in!")
        home_page.click_login()
        logging.info("Login page is opened")
        home_lgn_page.fill_and_submit_new_user_login_form(test_data.username, test_data.password)
        logging.info("Home page is opened")
        home_page.click_user_action_btn()
        logging.info("User action button is clicked!")
        account_balance = user_action_page.get_balance()
        logging.info(f"Balance is: {account_balance}")
        user_action_page.add_amount_and_submit_checkout_btn(test_data.amount)
        new_account_balance = user_action_page.get_balance()
        logging.info(f"New account balance is: {new_account_balance}")
        logging.info("New balance is correct")
        assert ((int(account_balance) + int(test_data.amount)) == int(new_account_balance))

    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test is completed")
        driver.quit()
        logging.info("All opened tabs are closed")


if __name__ == '__main__':
    test()
