from helpers.test_data import *
from library.general import *


def run_test():
    wait(driver, 10)
    run_driver(driver, practice_page_url)
    click_on_button(driver, alert_button)
    click_on_alert(driver, alert_button)
    click_on_button(driver, hide_button)
    style_attribute = get_style_attribute(hide_input_field_xpath)
    check_hidden(style_attribute)
    scroll_to_footer(driver, footer_text)
    print_text(driver, footer_text)
    click_on_button(driver, sign_in)
    fill_form(email_address, password, login_credentials['email'], login_credentials['password'])
    click_on_button(driver, login_button)
    change_tab(driver, 1)
    run_driver(driver, python_page_url)
    search(driver, search_input_field, 'Automation')
    click_on_button(driver, go_button)
    change_tab(driver, 0)
    close_browser(driver)


if __name__ == '__main__':
    run_test()

# Anna - No need keep locators.py file when use page object model, you keep locators in pages
# action.py file is additional, just to keep only one object, you could have  action = ActionChains(driver) in general helpers
# Where is your pages? maybe you deleted it after last commit?
# Code works, but page object model is not used
