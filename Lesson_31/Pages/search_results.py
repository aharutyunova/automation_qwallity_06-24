from selenium.webdriver.support.wait import WebDriverWait

from Lesson_31.Helpers.basic_page import Basic_Hepler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import logging


class SearchResultsPage(Basic_Hepler):
    BRAND_FILTER_LOC = (By.XPATH, "//*[@id='searchFilters']/div[1]/div[2]/section[3]/div[2]/ul/li[3]/a")
    PRICE_FILTER_LOC = (By.XPATH, "//*[@id='searchFilters']/div[1]/div[2]/section[4]/div/ul/li/a")
    RESULTS_LOC = (By.XPATH, "//*[@id='products']/article/a")

    def scroll_into_view_and_hover(self, locator, message):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        logging.info(message)

    def filter_by_brand(self, brand_name):
        brand_filter_elem = self.find_elem_ui(self.BRAND_FILTER_LOC)
        brand_filter_elem.send_keys(brand_name)
        brand_filter_elem.click()

    def filter_by_price(self, price_range):
        price_filter_elem = self.find_elem_ui(self.PRICE_FILTER_LOC)
        price_filter_elem.send_keys(price_range)
        price_filter_elem.click()

    def get_results(self):
        return self.find_elements(self.RESULTS_LOC)