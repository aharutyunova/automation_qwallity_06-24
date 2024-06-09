from selenium.webdriver.common.by import By
import logging
from test import BaseHelper  

class Test(BaseHelper): 

    hidden_el = (By.XPATH, '//*[@id="hide-textbox"]')

    def hide_element(self):
        self.find_and_click(self.hidden_el)
        logging.info('Successful!!! hidden element')

