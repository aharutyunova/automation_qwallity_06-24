from Helpers.basic_page import open_url
from Pages import home_p
from Pages import main_p
from Pages import login_p
from Pages import user_actions_p
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
            open_url(driver, config.url)
            assert (
                driver.current_url == "https://qwallity-prod.onrender.com/"
                ), f"Wrong URL{driver.current_url}"

            main_p.authorization(driver, test_data.email, test_data.code)
            logging.info(
                f"Authorization performed with email: {test_data.email}")
            assert (
                driver.current_url == "https://qwallity-prod.onrender.com/home"
            ), "Authorization Failed"

            home_p.go_to_login_form(driver)
            assert (
                driver.current_url == (
                    "https://qwallity-prod.onrender.com/login")
                ), f"Wrong URL{driver.current_url}"

            login_p.login(driver, test_data.username, test_data.password)
            assert (
                driver.current_url == "https://qwallity-prod.onrender.com/home"
            ), "Authorization Failed"

            home_p.go_to_user_actions(driver)
            assert (
                driver.current_url == (
                    "https://qwallity-prod.onrender.com/user_action"
                )), f"Wrong URL{driver.current_url}"

            acc_balance_before = user_actions_p.get_acc_balance(driver)
            user_actions_p.payment(driver, test_data.amount)
            acc_balance_after = user_actions_p.get_acc_balance(driver)
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

# Anna - good job, only in test case try don't use so many assertions, test case should check one max 2 main cases, so assert only that cases
# If you want to check that after click on element page is changed, don't assert every step in test case, check it in page functions
# for example in add payment method write all actionas and wait until url will be changed or any other element will be visible etc