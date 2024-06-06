import locators
from library import general

user_name_input_xpath = "//input[@id= 'username']"
password_input_xpath = "//input[@id= 'password-field']"
login_button_xpath = "//button[@type= 'submit']"


def sign_in(driver, user_name, password):
    general.fill_form(locators.email_input_xpath,
                      locators.code_input_xpath,
                      user_name,
                      password
                      )
    general.click_on_button(driver, locators.send_button_xpath)
