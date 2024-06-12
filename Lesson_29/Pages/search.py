from Helpers.basicHelper import Basic_Helper
from selenium.webdriver.common.by import By


class SearchPage(Basic_Helper):

    search_input_loc = (By.XPATH, "//input[@id='searchInp']")
    searched_brand_ddl_loc = (By.XPATH, "//li[@class='filter-models active']/div[@class='collapsible-header active']")
    search_result_loc = (By.XPATH, "//div[@id='search-result']")

    def searchInput(self, car_name):
        self.findandinput(self.search_input_loc, car_name)
        brand = self.find_element(self.searched_brand_ddl_loc).text
        return brand

    def searchresult(self):
        result = self.find_elements(self.search_result_loc)
        return result
    
    


