import locators
from library import general

email_input_xpath = '//*[@id="email"]'
code_input_xpath = '//*[@id="code"]'
send_button_xpath = '//*[@id="Send"]'


def main_sign_in(driver, main_user_name, main_password):
    general.fill_form(locators.user_name_input_xpath,
                      locators.password_input_xpath,
                      main_user_name,
                      main_password
                      )
    general.click_on_button(driver, locators.login_button_xpath)
    general.click_on_button(driver, locators.navigation_bar_login)
