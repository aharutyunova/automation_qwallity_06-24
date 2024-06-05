import time
from selenium.webdriver.common.action_chains import ActionChains
from Lesson_27.Helpers.basic_page import Basic_Helper
from selenium.webdriver.common.by import By
import logging


class Practise_Page(Basic_Helper):
    btn_alert_loc = (By.XPATH, "//input[@id='alertbtn']")
    hide_button_loc = (By.ID, "hide-textbox")
    mouse_hover_button_loc = (By.ID, "mousehover")
    top_option_loc = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
    footer_text_loc = (By.XPATH, "//*[@id='page']/div[3]/div/div/div[1]/div/div[1]/p")
    sign_in_btn_loc = (By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a')

    def save_alert_text(self):
        logging.info("Attempting to click the alert button")
        try:
            self.find_and_click(self.btn_alert_loc)
            alert = self.driver.switch_to.alert
            logging.info(f"Alert text: {alert.text}")
            alert.accept()
            logging.info("Alert accepted")
        except Exception as e:
            logging.error(f"Error clicking alert button: {str(e)}")

    def hide_element_check(self):
        logging.info("Attempting to click the hide button")
        try:
            self.find_and_click(self.hide_button_loc)
            elem = self.find_elem_dom((By.ID, "displayed-text"))
            assert "display: none;" in elem.get_attribute("style"), "Element is not hidden successfully"
            logging.info("Element is hidden successfully")
        except Exception as e:
            logging.error(f"Error hiding element: {str(e)}")

    def mouse_hover_check(self):
        logging.info("Attempting to hover over the mouse hover button")
        try:
            element = self.find_elem_ui(self.mouse_hover_button_loc)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            logging.info("Hovered over the Mouse Hover button")
            self.find_and_click(self.top_option_loc)
            logging.info("Clicked the top option")
        except Exception as e:
            logging.error(f"Error hovering over element: {str(e)}")

    def footer_text(self):
        logging.info("Scrolling to footer text")
        try:
            element = self.find_elem_ui(self.footer_text_loc)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            footer_text = element.text
            logging.info(f"Footer text: {footer_text}")
        except Exception as e:
            logging.error(f"Error getting footer text: {str(e)}")

    def sign_in(self, email, password):
        logging.info("Attempting to click the sign-in button")
        try:
            self.find_and_click(self.sign_in_btn_loc)
            logging.info("Sign-in button clicked, switching to new window")
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.find_and_send_keys((By.ID, "email"), email)
            self.find_and_send_keys((By.ID, "login-password"), password)
            self.find_and_click((By.XPATH, "//*[@id='login']"))
            time.sleep(5)
            logging.info("Sign-in form submitted")

        except Exception as e:
            logging.error(f"Error signing in: {str(e)}")

