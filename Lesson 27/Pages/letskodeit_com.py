from Helpers.basic_page import BasicHelper  # Importing the BasicHelper class from Helpers.basic_page module
from selenium.webdriver.common.by import By  # Importing By class for locating elements
from selenium.webdriver.common.keys import Keys  # Importing Keys class for keyboard interactions
import logging  # Importing the logging module for logging messages
from selenium.webdriver.common.action_chains import ActionChains  # Importing ActionChains for performing actions like mouse hover
import time  # Importing the time module for adding delays

class Letskodeit_Page(BasicHelper):  # Define a class Letskodeit_Page which inherits from BasicHelper
   
    # Define locators for various elements on the page
    btn_alert_loc = (By.ID, 'alertbtn')
    btn_hide_loc = (By.ID, 'hide-textbox')
    inp_hide_loc = (By.ID, 'displayed-text')
    btn_mouse_loc = (By.ID, 'mousehover')
    top_option_loc = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
    footer_txt_loc = (By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")
    btn_sign_in_loc = (By.XPATH, "//a[@href='/login']")

    # Method to click on an alert popup
    def click_alert_popup(self):
        alert = self.find_and_click(self.btn_alert_loc)  # Find and click the alert button
        logging.info("Clicked on  the Alert popup")
        alert = self.driver.switch_to.alert  # Switch to the alert
        alert_text = alert.text  # Get the text of the alert
        logging.info(f"Alert accepted with text: {alert_text}")
        alert.accept()  # Accept the alert

    # Method to hide an element and check if it's hidden
    def hide_element_and_check(self):
        self.find_and_click(self.btn_hide_loc)  # Find and click the hide button
        logging.info("Clicked on the Hide button")
        display_style = self.find_element_dom(self.inp_hide_loc).get_attribute('style')  # Get the style attribute of the hidden element
        logging.info(f"Hidden attribute is: {display_style}")
        logging.info("Element has been hidden")
        
    # Method to scroll to a mouse hover element and click on it
    def scroll_and_click_mouse_hover(self):
        btn_mous_el = self.find_element_ui(self.btn_mouse_loc)  # Find the mouse hover button
        actions = ActionChains(self.driver)  # Create an ActionChains object
        actions.move_to_element(btn_mous_el).perform()  # Move to the mouse hover button
        logging.info("Scrolled to Mouse Hover button")
        self.find_and_click(self.top_option_loc)  # Find and click the top option
        logging.info("Clicked on Top option")
        time.sleep(2)  # Add a delay to ensure the action is completed
        
    # Method to get and log the footer text
    def get_footer_text(self):
        footer_text = self.find_element_ui(self.footer_txt_loc).text  # Find the footer element and get its text
        logging.info(f"Footer displayed with text: {footer_text}")

    # Method to click on the Sign In button
    def click_sign_in(self):
        self.find_and_click(self.btn_sign_in_loc)  # Find and click the Sign In button
        logging.info("Clicked on the Sign In button")
