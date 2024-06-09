from general import url
import home
import main_page
import login
import test_scenario
import test_data
import config
from selenium import webdriver
import logging


def test():
    try:
        config.configure_logging()
        logging.info("Starting test")

        driver = webdriver.Chrome()
        logging.info("Chrome WebDriver initialized")

        try:
            url(driver, config.url)
            assert (
                driver.current_url == "https://qwallity-prod.onrender.com/"
                ), f"Wrong URL{driver.current_url}"

            main_page.authorization(driver, test_data.email, test_data.code)
            logging.info(
                f"Authorization performed with email: {test_data.email}")
            assert (
                driver.current_url == "https://qwallity-prod.onrender.com/home"
            ), "Authorization Failed"

            home.go_to_login_form(driver)
            assert (
                driver.current_url == (
                    "https://qwallity-prod.onrender.com/login")
                ), f"Wrong URL{driver.current_url}"

            login.login(driver, test_data.username, test_data.password)
            assert (
                driver.current_url == "https://qwallity-prod.onrender.com/home"
            ), "Authorization Failed"

            home.go_to_user_actions(driver)
            assert (
                driver.current_url == (
                    "https://qwallity-prod.onrender.com/user_action"
                )), f"Wrong URL{driver.current_url}"

            acc_balance_before = test_scenario.get_acc_balance(driver)
            test_scenario.payment(driver, test_data.amount)
            acc_balance_after = test_scenario.get_acc_balance(driver)
            logging.info(f"test_data.amount = {test_data.amount}")
            logging.info(f"balance before = {acc_balance_before}")
            logging.info(f"balance after = {acc_balance_after}")
            assert (
                (
                    int(acc_balance_before) + int(test_data.amount)
                ) == int(acc_balance_after)
            ), "Invalid balance"

        except Exception as e:
            logging.error(f"Error during test execution: {e}")

        input("press any key to continue...\n")
        driver.quit()
        logging.info("Browser closed")
    except Exception as e:
        logging.critical(f"Critical error: {e}")


if __name__ == '__main__':
    test()