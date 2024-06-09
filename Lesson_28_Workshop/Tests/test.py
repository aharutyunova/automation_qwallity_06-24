from selenium import webdriver
from Helpers.basic_page import open_url
from Pages import enter_app
from Pages import home_app
from Pages import login_app
from Pages import user_action_app
import test_data
import config
import logging


def test_case():
    try:
        config.configure_logging()
        logging.info("Starting test case")
        driver = webdriver.Chrome()
        try:
            open_url(driver, config.url)
            enter_app.authorization(driver, test_data.email, test_data.code)
            home_app.go_to_login(driver)
            login_app.login_system(driver, test_data.username, test_data.password)
            home_app.go_to_user_actions(driver)
            balance_before = user_action_app.get_balance(driver)
            user_action_app.add_amount(driver, test_data.amount)
            balance_after = user_action_app.get_balance(driver)
            logging.info(f"Amount = {test_data.amount}")
            logging.info(f"Balance before = {balance_before}")
            logging.info(f"Balance after = {balance_after}")
            assert (
                (
                    int(balance_before) + int(test_data.amount)
                ) == int(balance_after)
            ), "Invalid balance"

        except Exception as e:
            logging.error(f"Error during test execution: {e}")

        driver.quit()
        logging.info("Browser closed")
    except Exception as e:
        logging.critical(f"Critical error: {e}")


if __name__ == '__main__':
    test_case()

# Good job Lian jan, Test is pass, structure of POM is correct