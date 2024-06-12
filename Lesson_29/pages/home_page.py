from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.auto.am"
        self.search_input = (By.NAME, "category")

    def load(self):
        self.driver.get(self.url)

    def search_for_brand(self, brand_name):
        search_element = self.driver.find_element(*self.search_input)
        search_element.clear()
        search_element.send_keys(brand_name)
        search_element.send_keys(Keys.RETURN)