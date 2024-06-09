from Helpers.basic_page import Basic_Hepler
from Helpers import logging_config
from Pages.main import Main_Page
from Pages.login import Login_Page
from Pages.user_actions import User_Actions
import testdata
import config
import logging
from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    logging_config.configure_logging()
    bp = Basic_Hepler(driver)
    main_page = Main_Page(driver)
    login_page = Login_Page(driver)
    user_action = User_Actions(driver)
    bp.open_url(config.url)
    main_page.enter_to_qwallity()
    login_page.login()
    main_page.go_to_page('User_Action')
    before_amount = user_action.get_balance_value()
    user_action.add_balance(testdata.amount)
    after_amount = user_action.get_balance_value()
    assert before_amount + testdata.amount == after_amount, logging.error(f'{ before_amount + testdata.amount} is not equal to {after_amount}')
    logging.info(f'{ before_amount + testdata.amount} is equal to {after_amount}')
    logging.info("Test is Pass")


if __name__ == '__main__':
    test()
