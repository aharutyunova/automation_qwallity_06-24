import general
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import logging


email_loc = (By.XPATH, '//*[@id="email"]')
code_loc = (By.XPATH, '//*[@id="code"]')
btn_send_loc = (By.XPATH, '//*[@id="Send"]')


def authorization(driver, email, code):
    try:
        logging.info("Starting authorization process")

        general.find_and_send_keys(driver, email_loc, email)
        logging.info(f"Email entered: {email}")

        general.find_and_send_keys(driver, code_loc, code)
        logging.info(f"Code entered: {code}")

        general.find_and_click(driver, btn_send_loc)
        logging.info("Send button clicked")
    except Exception as e:
        logging.error(f"Error during authorization: {e}")


# Dear Anna, I used Lusines homework solution.

# Lian jan thanks for your honesty :)
# I hope even you re-used this solution you get the page object model idea and how it works
# I added comment under Lusine solution, you can have a look ;)