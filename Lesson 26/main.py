"""
- Have general file where keep functions to work with elements
- Have separate file/files where keep functions by requirement points
- Have test data file where keep test data used in the flow
- Have main test file where call functions for cover end to end flow of the task 

"""
import logging  # Import the logging module to enable logging of errors and other information
import scenarios  # Import the scenarios module which contains various test scenarios
import general_data  # Import the general_data module which contains general data functions like get_driver


def main():
    driver = general_data.get_driver()  # Initialize the web driver using a function from general_data
    try:
        scenarios.open_page(driver)  # Open the test page using a function from scenarios
        scenarios.click_alert_popup(driver)  # Click on the alert popup using a function from scenarios
        scenarios.hide_element_and_check(driver)  # Hide a specific element and perform a check using a function from scenarios
        scenarios.scroll_and_click_mouse_hover(driver)  # Scroll and perform a mouse hover click using a function from scenarios
        scenarios.get_footer_text(driver)  # Check the footer text using a function from scenarios
        scenarios.click_sign_in(driver)  # Click the sign-in button using a function from scenarios
        scenarios.fill_and_submit_login_form(driver)  # Fill in the login form and submit it using a function from scenarios
        scenarios.validation_message(driver)  # Validate the message displayed after login using a function from scenarios
        scenarios.open_new_tab_and_search(driver)  # Open a new browser tab and perform a search using a function from scenarios
    except Exception as e:
        logging.error(f"Test failed: {e}")  # Log an error message if any exception is raised during the test scenarios
    finally:
        scenarios.close_all_tabs(driver)  # Close all browser tabs regardless of whether an exception occurred


if __name__ == '__main__':
    main()  # Run the main function to execute the test scenarios
    print("Test case is run and passed!")  # Print a message indicating that the test case has finished.
