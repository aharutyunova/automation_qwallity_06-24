import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from general import (
    logger, find_and_click, find_and_send_keys, find_element_ui,
    find_element_dom, find_elements
)
from locators import (
    btn_alert_loc, hide_button_loc, mouse_hover_button_loc, top_option_loc,
    footer_text_loc, sign_in_btn_loc, validation_msg_loc, search_box_loc
)


def save_alert_text(driver):
    find_and_click(driver, btn_alert_loc)
    al = driver.switch_to.alert
    logger.info(f"Alert text: {al.text}")
    al.accept()


def hide_element_check(driver):
    find_and_click(driver, hide_button_loc)
    element = find_element_dom(driver, (By.ID, "displayed-text"))
    assert "display: none;" in element.get_attribute("style"), "Element is hidden successfully"
    logger.info("Element is hidden successfully")


def mouse_hover_check(driver):
    element = find_element_ui(driver, mouse_hover_button_loc)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    logger.info("Hovered over the Mouse Hover button")
    find_and_click(driver, top_option_loc)


def footer_text(driver):
    element = find_element_ui(driver, footer_text_loc)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    footer_text = element.text
    logger.info(f"Footer text: {footer_text}")


def sign_in(driver):
    find_and_click(driver, sign_in_btn_loc)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    find_and_send_keys(driver, (By.ID, "email"), "incorrect@email.com")
    find_and_send_keys(driver, (By.XPATH, "//*[@id='login-password']"), "incorrectpassword")
    find_and_click(driver, (By.XPATH, "//*[@id='login']"))
    validation_text = find_element_ui(driver, validation_msg_loc).text.strip()
    logger.info(f"Validation message: {validation_text}")


def python_search(driver):
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    logger.info("Switched to the new tab")
    driver.get("https://www.python.org/")
    search_box = find_element_ui(driver, search_box_loc)
    search_box.send_keys("Automation")
    search_box.send_keys(Keys.RETURN)
    results = find_elements(driver, (By.CSS_SELECTOR, ".list-recent-events > li"))
    num_results = len(results)
    logger.info(f"Number of search results on the first page: {num_results}")
