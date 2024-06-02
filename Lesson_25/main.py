import logging 
import os
import general
import config
import locators


path = os.getcwd()
full_path = os.path.join(path, 'Lesson_25')
os.chdir(full_path)

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log_Lesson_25.log', 
                    filemode='w+', 
                    encoding='utf-8')

try:
    # 1. Open Chrome browser
    driver = general.getdriver()
    driver.maximize_window()
    # 2. Navigate to https://www.letskodeit.com/practice
    general.geturl(driver,config.url)
    # 3. Click to open the Alert popup
    general.findandclick(driver, locators.alert_loc)
    # 4. Get text from the popup and log it
    general.swithtoalert(driver)
    #5. Locate the following element, hide it, check element is hidden
    if general.locelement(driver, locators.hide_show_text_loc):
        general.findandclick(driver, locators.hide_btn)
        hidden_text = general.locelement(driver,locators.hide_show_text_loc)
        hidden_text_attribute_value = hidden_text.get_attribute('style')
        general.assertion(config.expected_attr_value_of_hid_el, hidden_text_attribute_value)
    else:
        logging.info("hide_show_text_loc locator not found element")
    #  7. Scroll and click to the Mouse Hover button and Click on Top option to go to the top of screen
    elem = general.scrolluntilelement(driver, locators.mouse_hover_btn)
    general.hoveronandselectoption(driver, locators.mouse_hover_top, elem)

    # 8. Go to the footer and log footer text
    footer = general.scrolluntilelement(driver, locators.footer_loc)
    logging.info(footer.text)
    
    # 9. Click on the Sign In button
    general.findandclick(driver, locators.signIn_btn)
    
    # 10. Fill the fields with incorrect email or password and click the LogIn button
    general.findandinput(driver, locators.email, config.email)
    general.findandinput(driver, locators.password, config.password)
    general.findandclick(driver, locators.login_btn)

    # 11. Get validation message and log it
    validation = general.locelement(driver, locators.incorrect_login_text_loc)
    message = validation.text
    logging.info(f"Validation message for incorrect login: {message}")

    # 12. Open a new tab, switch to the new tab
    original_window = general.newtab(driver)

    # 13. Get https://www.python.org/ on the second tab
    general.geturl(driver,config.python_url)

    # 14. Search the 'Automation’ word
    general.findandinput(driver,locators.search_loc, config.search_text)
    general.findandclick(driver,locators.submit_search)

    # 15. Write in the log file how many results is found on the first page
    result_count = len(driver.find_elements(*locators.search_result_loc))
    logging.info(f"Search result count on first page is {result_count}")

    # 16. Come back to the first tab
    driver.switch_to.window(original_window)

    #17. Close all opened tabs
    general.closealltabs(driver)

except Exception:
    logging.error("An unexpected error occurred somewhere")
finally:
    driver.quit()
