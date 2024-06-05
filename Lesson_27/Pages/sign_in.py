from selenium.webdriver.common.by import By
from Lesson_27.Helpers.basic_page import Basic_Helper
import logging


class Sign_In_Page(Basic_Helper):
    email_field_loc = (By.ID, "email")
    password_field_loc = (By.ID, "login-password")
    login_button_loc = (By.ID, "login")  # Adjust the locator as needed
    validation_msg_loc = (By.XPATH, "//*[@id='validation-message']")

    def sign_in(self, email, password):
        logging.info("Attempting sign-in process")
        try:
            self.find_and_send_keys(self.email_field_loc, email)
            self.find_and_send_keys(self.password_field_loc, password)
            self.find_and_click(self.login_button_loc)
            validation_text = self.find_elem_ui(self.validation_msg_loc).text.strip()
            logging.info(f"Validation message: {validation_text}")
        except Exception as e:
            logging.error(f"Error signing in: {str(e)}")
