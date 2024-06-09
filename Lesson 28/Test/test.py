
import sys
import os

# Ensure the root directory is in the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules and classes
from Helpers.basic_page import BasicHelper
from Helpers import logging_config
from Pages.main_page import Main_Page
from Pages.home_page import Home_Page
from Pages.login_page import Login_Page
from Pages.user_action_page import User_Action_Page
import test_data
import config_data
from selenium import webdriver
import logging


def test():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    bh = BasicHelper(driver)
    main_login_page = Main_Page(driver)
    home_page = Home_Page(driver)
    login_page = Login_Page(driver)
    user_act_page = User_Action_Page(driver)

    try:
         # Step 1: Open the main URL
        bh.open_base_url(config_data.base_url)
        # Step 2: Fill and submit the main login form
        main_login_page.fill_and_submit_login_form(test_data.user_email, test_data.password_code)
        # Step 3: Click the login button to proceed
        home_page.click_login_btn()
        logging.info("Login page opened")
        # Step 4: Fill and submit the second login form with custom user credentials
        login_page.fill_and_submit_second_login_form(test_data.username, test_data.password)
        logging.info("Home page opened")
        # Step 5: Click the user action button to proceed
        home_page.click_user_action_btn()
        logging.info("User Action page opened")
        # Step 6: Get the initial account balance
        acc_balance = user_act_page.get_balance()
        logging.info(f"Balance is: {acc_balance}")
        # Step 7: Add amount and submit the checkout form
        user_act_page.add_amount_and_submit_checkout_btn(test_data.amount)
        # Step 8: Get the new account balance
        new_acc_balance = user_act_page.get_balance()
        logging.info(f"New Account Balance is: {new_acc_balance}")
        logging.info("New balance is correct")
        # Step 9: Validate the account balance after transaction
        assert ((int(acc_balance) + int(test_data.amount)) == int(new_acc_balance))
    
    except Exception as e:
        # Log any exceptions that occur
        logging.error(f"Test failed: {e}")
        
    finally:
        # Ensure the WebDriver is closed
        logging.info("Test is completed")
        driver.quit()
        logging.info("Closed all opened tabs")

if __name__ == '__main__':
    test()

# Anna everything is correct good solution. Only ine note don't keep config_data and test_data in test folder, keep it as separate files