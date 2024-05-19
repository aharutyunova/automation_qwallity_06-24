from selenium import webdriver
from selenium.webdriver.common.by import By

browsers = ["Chrome", "Firefox"]
driver = webdriver.Chrome()
drivers = [webdriver.Chrome(), webdriver.Firefox()]
driver.get("https://www.python.org/")
driver.maximize_window()
search = driver.find_element(By.ID, "id-search-field")
search.send_keys("bla bla")
go_button = driver.find_element(By.ID, "submit")
go_button.click()
go_button = driver.find_element_by_xpath("//button[@type='submit']")
go_button.click()
no_results_found = driver.find_element
assert "No results found."
print(error)