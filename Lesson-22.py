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

# Anna - when you write drivers = [webdriver.Chrome(), webdriver.Firefox()], you open 2 drivers in the same time
# But it is not so big issue, you have find_element_by_xpath in line 13, but selenium 4 support only
# driver.find_element(By.XPATH, "//button[@type='submit']") syntax
# In line 15 you have driver.find_element but don't give which element you want to find, you should give something like
#  no_results_found = driver.find_element(BY.XPATH, 'any xpath....').text 
# Then assert "No results found."== no_results_found