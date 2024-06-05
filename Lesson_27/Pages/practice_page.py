from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.common.action_chains import ActionChains
import time


class Practice_Page(BasicHelper):
    # Locators
    btn_alert = (By.XPATH, "//input[@id='alertbtn']")
    btn_hide = (By.XPATH, "//input[@id='hide-textbox']")
    inp_hide = (By.XPATH, "//input[@id='displayed-text']")
    btn_mous = (By.XPATH, "//button[@id='mousehover']")
    top_option = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
    txt_footer = (By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")
    btn_sign_in = (By.XPATH, "//a[@href='/login']")

    def click_alert_popup(self):
        alert = self.find_and_click(self.btn_alert)
        logging.info("Clicked to open the Alert popup")
        alert = self.driver.switch_to.alert
        logging.info(f"Alert popup text: {alert.text}")
        alert.accept()

    def hide_element_and_check(self):
        self.find_and_click(self.btn_hide)
        logging.info("Clicked Hide button")
        hide_attr = self.find_elem_dom(self.inp_hide).get_attribute('style')
        logging.info(f"Hidden attribute is: {hide_attr}")
        logging.info("Text box is hidden as expected")
        
    def scroll_and_click_mouse_hover(self):
        btn_mous_el = self.find_elem_ui(self.btn_mous)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn_mous_el).perform()
        logging.info("Scrolled to Mouse Hover button")
        self.find_and_click(self.top_option)
        logging.info("Clicked on Top option")
        time.sleep(2)
        
    def get_footer_text(self):
        footer_txt = self.find_elem_ui(self.txt_footer).text
        logging.info(f"Footer text: {footer_txt}")

    def click_sign_in(self):
        self.find_and_click(self.btn_sign_in)
        logging.info("Clicked on Sign In button")
