from Lesson_31.Helpers.basic_page import Basic_Hepler
from selenium.webdriver.common.by import By


class MainPage(Basic_Hepler):
    SEARCH_BOX = (By.XPATH, "//*[@id='searchAll']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='searchForm']/button")

    def search_product(self, product_name):
        self.find_and_send_keys(self.SEARCH_BOX, product_name)
        self.find_and_click(self.SEARCH_BUTTON)