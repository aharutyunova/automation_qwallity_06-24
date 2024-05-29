from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def open_practice_page():
    driver.get("https://www.letskodeit.com/practice")
    driver.maximize_window()
    logging.info("Opened LetsKodeIt Practice page")


def click_alert_popup():
    btn_alert_loc = (By.XPATH, "//input[@id='alertbtn']")
    btn_alert_el = wait.until(EC.element_to_be_clickable(btn_alert_loc))
    btn_alert_el.click()
    logging.info("Clicked to open the Alert popup")
    alert = driver.switch_to.alert
    logging.info(f"Alert popup text: {alert.text}")
    alert.accept()


def hide_element_and_check():
    btn_hide_loc = (By.XPATH, "//input[@id='hide-textbox']")
    inp_hide_loc = (By.XPATH, "//input[@id='displayed-text']")
    btn_hide_el = wait.until(EC.element_to_be_clickable(btn_hide_loc))
    btn_hide_el.click()
    logging.info("Clicked Hide button")
    text_box = driver.find_element(*inp_hide_loc)
    if not text_box.is_displayed():
        logging.info("Text box is hidden as expected")
    else:
        logging.warning("Text box is not hidden")


def scroll_and_click_mouse_hover():
    btn_mous_loc = (By.XPATH, "//button[@id='mousehover']")
    top_option_loc = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
    btn_mous_el = driver.find_element(*btn_mous_loc)
    actions = ActionChains(driver)
    actions.move_to_element(btn_mous_el).perform()
    logging.info("Scrolled to Mouse Hover button")
    top_option_el = wait.until(EC.element_to_be_clickable(top_option_loc))
    top_option_el.click()
    logging.info("Clicked on Top option")
    time.sleep(2)


def footer_text():
    footer_text_loc = (By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")
    footer_text_el = driver.find_element(*footer_text_loc).text
    logging.info(f"Footer text: {footer_text_el}")


def click_sign_in():
    btn_sign_in_loc = (By.XPATH, "//a[@href='/login']")
    btn_sign_in_el = wait.until(EC.element_to_be_clickable(btn_sign_in_loc))
    btn_sign_in_el.click()
    logging.info("Clicked on Sign In button")


def fill_and_submit_login_form():
    email_fld_loc = (By.XPATH, "//input[@placeholder='Email Address']")
    pass_fld_loc = (By.XPATH, "//input[@id='login-password']")
    email_fld_data = "incorrect_email@gmail.com"
    pass_fld_data = "incorrect_password"
    btn_login_loc = (By.XPATH, "//button[@id='login']")
    email_fld_el = wait.until(EC.element_to_be_clickable(email_fld_loc))
    email_fld_el.send_keys(email_fld_data)
    pass_fld_el = driver.find_element(*pass_fld_loc)
    pass_fld_el.send_keys(pass_fld_data)
    login_button = driver.find_element(*btn_login_loc)
    login_button.click()
    logging.info("Filled incorrect email and password, "
                 "and clicked LogIn button")


def validation_message():
    msg_valid_loc = (By.XPATH, "//span[@id='incorrectdetails']")
    msg_valid_el = wait.until(EC.visibility_of_element_located(msg_valid_loc)).text
    logging.info(f"Validation message: {msg_valid_el}")


def open_new_tab_and_search():
    new_tab_url = "https://www.python.org/"
    driver.execute_script("window.open('')")
    before = driver.window_handles[0]
    after = driver.window_handles[-1]
    driver.switch_to.window(after)
    logging.info("Opened a new tab and switched to it")
    driver.get(new_tab_url)
    logging.info("Navigated to https://www.python.org/ on the second tab")
    fld_search_loc = (By.XPATH, "//input[@id='id-search-field']")
    search_text = "Automation"
    btn_search_loc = (By.XPATH, "//button[@id='submit']")
    fld_search_el = wait.until(EC.element_to_be_clickable(fld_search_loc))
    fld_search_el.send_keys(search_text)
    btn_search_el = driver.find_element(*btn_search_loc)
    btn_search_el.click()
    logging.info("Searched for the word 'Automation'")
    results_loc = (By.XPATH, '//div[@id="content"]//li')
    results_el = driver.find_elements(*results_loc)
    logging.info(f"Number of results found on the first page: {len(results_el)}")
    driver.switch_to.window(before)
    logging.info("Switched back to the first tab")


def close_all_tabs():
    driver.quit()
    logging.info("Closed all opened tabs")


def main():
    try:
        open_practice_page()
        click_alert_popup()
        hide_element_and_check()
        scroll_and_click_mouse_hover()
        footer_text()
        click_sign_in()
        fill_and_submit_login_form()
        validation_message()
        open_new_tab_and_search()
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        close_all_tabs()


if __name__ == '__main__':
    main()
