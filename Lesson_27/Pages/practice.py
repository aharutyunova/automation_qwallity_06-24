from Helpers.basic_practice import Basic_Helper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


class Practice_Page(Basic_Helper):

    alert_loc = (By.XPATH, "//input[@id='alertbtn']")
    hide_show_text_loc = (By.XPATH, "//input[@id='displayed-text']")
    hide_btn = (By.XPATH, "//input[@id='hide-textbox']")
    show_btn = (By.XPATH, "//input[@id='show-textbox']")
    mouse_hover_top = (By.XPATH, "//div[@class ='mouse-hover-content']/a[@href ='#top']")
    mouse_hover_btn = (By.XPATH, "//button[@id = 'mousehover']")
    footer_loc = (By.XPATH, "//p[@class = 'small dynamic-text jqCopyRight']")
    signIn_btn = (By.XPATH, "//a[@href = '/login']")
    
    expected_attr_value_of_hid_el = 'display: none;'

    def locateAndHideEl(self):
        if Basic_Helper.locelement(self.driver, self.hide_show_text_loc):
            Basic_Helper.findandclick(self.driver, self.hide_btn)
            hidden_text = Basic_Helper.locelement(self.driver,self.hide_show_text_loc)
            hidden_text_attribute_value = hidden_text.get_attribute('style')
            Basic_Helper.assertion(self.expected_attr_value_of_hid_el, hidden_text_attribute_value)
        else:
            logging.info("hide_show_text_loc locator not found element")
    
    def goTopOfScreen(self):
        elem = Basic_Helper.scrolluntilelement(self.driver, self.mouse_hover_btn)
        Basic_Helper.hoveronandselectoption(self.driver, self.mouse_hover_top, elem)
    
