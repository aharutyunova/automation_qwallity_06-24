from selenium import webdriver
import config
from logging_config import configure_logging
from Helpers import basic_page
from Pages import login
from Pages import practice
from Pages import python_org
import test_data


def test():
    configure_logging()

    driver = webdriver.Chrome()

    url = config.url
    basic_page.open_url(driver, url)

    practice.txt_from_alert(driver)
    practice.hide_element(driver)  # here I'm getting error
    practice.scroll_and_mouse_hover(driver)
    practice.footer_text(driver)
    practice.sign_in(driver)
    login.login(driver, test_data.email, test_data.password)  # here I'm getting error

    basic_page.open_new_tab_and_switch_to_it(driver)
    driver.get('https://www.python.org/')
    python_org.searching_in_Python_org(driver, test_data.word)
    python_org.search_result(driver)

    basic_page.go_to_the_first_page(driver)

    input("Please enter any key to continue...\n")
    driver.quit()


if __name__ == "__main__":
    test()

# Anna jan I couldn't realise why I'm getting errors on my mentioned above lines

# Lusine jan you get error because when click on hide button, after it input field is hidden, then you try find element in ui and get exception
# But because you added this code in try except block it is not failed with timeout exception
# I changed find_element_ui to find_element_dom (to wait until element be exist in dom, not diplayed)
# Also in your test_data.py file, email is not with correct format. 
# I changed it, but it depends what you want to check, incorrect format message, or incorrect username message
