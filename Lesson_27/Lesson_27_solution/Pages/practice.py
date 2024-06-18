from Helpers import basic_page
from selenium.webdriver.common.by import By
import time
import logging


alert_loc = (By.XPATH, '//*[@id="alertbtn"]')
hidden_el_loc = (By.XPATH, '//*[@id="hide-textbox"]')
hidden_inp_field_loc = (By.XPATH, '//*[@id="displayed-text"]')
btn_mouse_hover_loc = (By.XPATH, '//*[@id="mousehover"]')
btn_top_in_mouse_hover_loc = (By.XPATH, '//*[@class="mouse-hover-content"]/a')
txt_footer_loc = (By.XPATH, '//p[@class="small dynamic-text jqCopyRight"]')
btn_sign_in_loc = (By.XPATH, '//*[@id="navbar-inverse-collapse"]/div')

try:
    def txt_from_alert(driver):
        try:
            alrt = basic_page.find_and_click(driver, alert_loc)
            alrt = driver.switch_to.alert
            txt_alrt = alrt.text
            alrt.accept()
            logging.info(txt_alrt)
        except Exception as e:
            logging.error(f'Error occurred{e}')

    def hide_element(driver):
        try:
            basic_page.find_and_click(driver, hidden_el_loc)

            inp_field = basic_page.find_elem_dom(driver, hidden_inp_field_loc)
            show_attr = inp_field.get_attribute('style')

            assert 'display: none' in show_attr, (
                "Failed - input field should be hidden")
            logging.info('Pass - input field is hidden')
        except Exception as e:
            logging.error(f'Error occurred{e}')

    def scroll_and_mouse_hover(driver):
        try:
            btn_mouse_hover = basic_page.find_elem_ui(
                driver, btn_mouse_hover_loc)
            driver.execute_script(
                "arguments[0].scrollIntoView(true);", btn_mouse_hover)
            logging.info(
                f"Scrolled to element: {btn_mouse_hover_loc}")

            basic_page.find_and_click(driver, btn_mouse_hover_loc)
            basic_page.find_and_click(driver, btn_top_in_mouse_hover_loc)
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def footer_text(driver):
        try:
            txt_footer = basic_page.find_elem_ui(driver, txt_footer_loc)
            driver.execute_script(
                "arguments[0].scrollIntoView(true);", txt_footer)
            logging.info(txt_footer.text)
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    def sign_in(driver):
        try:
            time.sleep(2)
            basic_page.find_and_click(driver, btn_sign_in_loc)
        except Exception as e:
            logging.error(f"Error occurred: {e}")


except Exception as e:
    logging.error(f'Error occurred: {e}')
