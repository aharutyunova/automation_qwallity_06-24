from selenium.webdriver.common.by import By


class SearchResultsPage:
    
    
    def __init__(self, driver):
        self.driver = driver
    
    result_locator = (By.CLASS_NAME, "search-result") 
        
    def get_results(self):
        return self.driver.find_elements(*self.result_locator) # Anna - with this locator no element is found

    def has_results(self):
        return len(self.get_results())

