from helpers.driver import driver

user_action_button = "//a[@href= '/user_action']"
account_balance_xpath = '//*[@id="acc_balance"]'
amount = '//*[@id="amount"]'
payment_method_xpath = '//*[@id="payment"]'
checkout_button = '//*[@id="Submit"]'


def get_current_balance(driver, balance_xpath):
    return balance_xpath.text()


get_current_balance(driver, account_balance_xpath)
