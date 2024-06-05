from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import test_data
import loc_data
import general_data

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: Navigate to the URL
def open_page(driver):
    driver.get(test_data.current_url)
    driver.maximize_window()
    logging.info("Navigated to letskodeit.com/practice page")

# Step 2: Wait for the "Alert" button to be clickable and click it to open the alert popup and get the text
def click_alert_popup(driver):
    general_data.find_and_click(driver, loc_data.btn_alert_loc)
    logging.info("Clicked on the Alert button")
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    logging.info(f"Alert accepted with text: {alert_text}")

# Step 3: Check if the element is hidden
def hide_element_and_check(driver):
    general_data.find_and_click(driver, loc_data.btn_hide_loc)
    logging.info("Clicked on the Hide button")
    display_style = general_data.find_elem_dom(driver, loc_data.inp_hide_loc).get_attribute('style')
    logging.info(f"Hidden attribute is: {display_style}")
    logging.info("Element has been hidden")
    
# Step 4: Scroll to the Mouse Hover button and perform mouse hover action and click the 'Top' option
def scroll_and_click_mouse_hover(driver):
    mouse_hover_button = general_data.find_element_ui(driver, loc_data.btn_mouse_loc)
    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover_button).perform()
    logging.info("Performed mouse hover action on Mouse Hover button")
    general_data.find_and_click(driver, loc_data.top_option_loc)
    logging.info("Clicked on the 'Top' option")
    time.sleep(3)

# Step 5: Scroll to the Footer element and log its text
def get_footer_text(driver):
    footer_text = general_data.find_element_ui(driver, loc_data.footer_txt_loc).text
    logging.info(f"Footer displayed with text: {footer_text}")

# Step 6: Click on the Sign in button
def click_sign_in(driver):
    general_data.find_and_click(driver, loc_data.btn_sign_in_loc)
    logging.info("Clicked on Sign In button")

# Step 7: Fill the email and password fields with incorrect credentials and click on the Log In button
def fill_and_submit_login_form(driver):
    general_data.find_and_send_keys(driver, loc_data.email_fld_loc, test_data.email)
    general_data.find_and_send_keys(driver, loc_data.password_fld_loc, test_data.password)
    general_data.find_and_click(driver, loc_data.btn_login_loc)
    logging.info("Filled incorrect email and password, and clicked on the LogIn button")

# Step 8: Log the validation message
def validation_message(driver):
    valid_msg = general_data.find_element_ui(driver, loc_data.msg_valid_loc).text
    logging.info(f"Validation message: {valid_msg}")

# Step 9: Open and switch to the new tab
def open_new_tab_and_search(driver):
    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[-1])
    logging.info("Opened a new tab and switched to it")
    driver.get(test_data.next_url)
    logging.info("Navigated to https://www.python.org/ on the second tab")
    general_data.find_and_send_keys(driver, loc_data.fld_search_loc, test_data.search_text)
    general_data.find_and_click(driver, loc_data.btn_search_loc)
    logging.info("Searched for the word 'Automation'")

    results_el = general_data.find_elements(driver, loc_data.results_loc)
    logging.info(f"Number of results found on the first page: {len(results_el)}")
    driver.switch_to.window(driver.window_handles[0])
    logging.info("Switched back to the first tab")

# Step 10: Close all tabs and the browser
def close_all_tabs(driver):
    driver.quit()
    logging.info("Closed all opened tabs")