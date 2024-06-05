from selenium.webdriver.common.by import By
from Lesson_27.Helpers.basic_page import Basic_Helper
import logging


class Sign_In_Page(Basic_Helper):
    email_field_loc = (By.ID, "email")
    password_field_loc = (By.ID, "login-password")
    login_button_loc = (By.ID, "login")  # Adjust the locator as needed
    validation_msg_loc = (By.XPATH, "//*[@id='incorrectdetails']")

    def sign_in(self):
        logging.info("Attempting sign-in process")
        try:
            validation_text = self.find_elem_ui(self.validation_msg_loc).text.strip()
            logging.info(f"Validation message: {validation_text}")

        except Exception as e:
            logging.error(f"Error signing in: {str(e)}")
