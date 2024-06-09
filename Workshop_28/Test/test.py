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
    driver = webdriver.Chrome()
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

        # Get the current balance
        account_balance = user_action_page.get_balance()
        logging.info(f"Current balance is: {account_balance}")

        # Convert the balance to a numerical value
        current_balance = float(account_balance.replace(',', '').replace('$', ''))  # Adjust as per the format

        # Add the new amount
        amount_to_add = float(test_data.amount)
        user_action_page.add_amount_and_submit_checkout_btn(test_data.amount)
        logging.info(f"Amount {amount_to_add} added and checkout button is clicked")

        # Get the new balance
        new_account_balance = user_action_page.get_balance()
        logging.info(f"New account balance is: {new_account_balance}")

        # Convert the new balance to a numerical value
        new_balance = float(new_account_balance.replace(',', '').replace('$', ''))  # Adjust as per the format

        # Verify the new balance is the sum of the current balance and the added amount
        expected_balance = current_balance + amount_to_add
        assert new_balance == expected_balance, f"Expected balance {expected_balance}, but got {new_balance}"
        logging.info("New balance is correct and verified")

    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        logging.info("Test is completed")
        driver.quit()
        logging.info("All opened tabs are closed")


if __name__ == '__main__':
    test()
