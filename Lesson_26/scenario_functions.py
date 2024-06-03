from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import test_data
import locators
import general

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def open_practice_page(driver):
    driver.get(test_data.url)
    driver.maximize_window()
    logging.info("Opened LetsKodeIt Practice page")


def click_alert_popup(driver):
    general.find_and_click(driver, locators.btn_alert_loc)
    logging.info("Clicked to open the Alert popup")
    alert = driver.switch_to.alert
    logging.info(f"Alert popup text: {alert.text}")
    alert.accept()


def hide_element_and_check(driver):
    general.find_and_click(driver, locators.btn_hide_loc)
    logging.info("Clicked Hide button")
    hide_attr = general.find_elem_dom(driver, locators.inp_hide_loc).get_attribute('style')
    logging.info(f"hidden attribute is: {hide_attr}")
    

def scroll_and_click_mouse_hover(driver):
    btn_mous_el = general.find_elem_ui(driver, locators.btn_mous_loc)
    actions = ActionChains(driver)
    actions.move_to_element(btn_mous_el).perform()
    logging.info("Scrolled to Mouse Hover button")
    general.find_and_click(driver, locators.top_option_loc)
    logging.info("Clicked on Top option")
    time.sleep(2)


def footer_text(driver):
    footer_text = general.find_elem_ui(driver, locators.footer_text_loc).text
    logging.info(f"Footer text: {footer_text}")


def click_sign_in(driver):
    general.find_and_click(driver, locators.btn_sign_in_loc)
    logging.info("Clicked on Sign In button")


def fill_and_submit_login_form(driver):
    general.find_and_send_keys(driver, locators.email_fld_loc, test_data.email_data)
    general.find_and_send_keys(driver, locators.pass_fld_loc, test_data.pass_data)
    general.find_and_click(driver, locators.btn_login_loc)
    logging.info("Filled incorrect email and password, and clicked LogIn button")


def validation_message(driver):
    valid_msg = general.find_elem_ui(driver, locators.msg_valid_loc).text
    logging.info(f"Validation message: {valid_msg}")


def open_new_tab_and_search(driver):
    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[-1])
    logging.info("Opened a new tab and switched to it")
    driver.get(test_data.new_tab_url)
    logging.info("Navigated to https://www.python.org/ on the second tab")
    general.find_and_send_keys(driver, locators.fld_search_loc, test_data.search_data)
    general.find_and_click(driver, locators.btn_search_loc)
    logging.info("Searched for the word 'Automation'")

    results_el = general.find_elements(driver, locators.results_loc)
    logging.info(f"Number of results found on the first page: {len(results_el)}")
    driver.switch_to.window(driver.window_handles[0])
    logging.info("Switched back to the first tab")


def close_all_tabs(driver):
    driver.quit()
    logging.info("Closed all opened tabs")
