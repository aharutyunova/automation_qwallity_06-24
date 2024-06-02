import general
import scenario_functions
import test_data


def real_test_scenario():
    driver = general.initialize_driver()
    driver.get(test_data.url)
    driver.maximize_window()

    try:
        scenario_functions.save_alert_text(driver)
        scenario_functions.hide_element_check(driver)
        scenario_functions.mouse_hover_check(driver)
        scenario_functions.footer_text(driver)
        scenario_functions.sign_in(driver)
        scenario_functions.python_search(driver)
    finally:
        if driver:
            general.close_driver(driver)


if __name__ == "__main__":
    real_test_scenario()
    print("This test case is finished successfully and no errors occur!")



# Ann jan did not know whether we need to change file names or not,
# I used the ones you used
# and also some scripts is taken from your solution
# workshop 26 would do but not today

# Anna - Even you took some parts from my solution, anyway it's good job.
# Exactly what I expect