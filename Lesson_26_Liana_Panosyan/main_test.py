import general
import test_data
import scenario_functions


def live_coding_scenario():
    driver = general.get_driver()
    driver.get(test_data.url)
    driver.maximize_window()
    scenario_functions.alert_text(driver)
    scenario_functions.hide_element(driver)
    scenario_functions.mouse_hover(driver)
    scenario_functions.footer_text(driver)
    scenario_functions.sign_in(driver)
    scenario_functions.python_search(driver)

    if driver:
        driver.quit()


if __name__ == "__main__":
    live_coding_scenario()
    print("Test case finished")

#  Anna - Lian jan this part is good enough, All that's left to do is spread it out by pages :)