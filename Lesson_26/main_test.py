import logging
import scenario_functions
import general


def main():
    driver = general.get_driver()
    try:
        scenario_functions.open_practice_page(driver)
        scenario_functions.click_alert_popup(driver)
        scenario_functions.hide_element_and_check(driver)
        scenario_functions.scroll_and_click_mouse_hover(driver)
        scenario_functions.footer_text(driver)
        scenario_functions.click_sign_in(driver)
        scenario_functions.fill_and_submit_login_form(driver)
        scenario_functions.validation_message(driver)
        scenario_functions.open_new_tab_and_search(driver)
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        scenario_functions.close_all_tabs(driver)


if __name__ == '__main__':
    main()
    print("Test case finished!")
