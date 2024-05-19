from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.python.org/")
time.sleep(2)
search = driver.find_element(By.ID, "id-search-field")
search.send_keys("bla-bla")
submit = driver.find_element(By.ID, "submit")
submit.click()

time.sleep(2)

results = driver.find_element(By.CSS_SELECTOR, ".list-recent-events").text
assert "No results found." in results

driver.close()
print("Test is finsihed.")


# I tried using a for cycle, but it didn't work for me. That's why I commented it.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drivers = [
    webdriver.Chrome,
    webdriver.Firefox
]
for driver_class in drivers:
    driver = driver_class()
    driver.maximize_window()


driver.get("https://www.python.org/")
time.sleep(2)
search = driver.find_element(By.ID, "id-search-field")
search.send_keys("bla-bla")
submit = driver.find_element(By.ID, "submit")
submit.click()

time.sleep(2)

results = driver.find_element(By.CSS_SELECTOR, ".list-recent-events").text
assert "No results found." in results

driver.close()
print("Test is finsihed.")
"""


# Anna - for one browser actions are correct, only you didn't use exceptions and logging, for loop you could write like this
"""
browsers = ['Chrome', 'Firefox']

for browser in browsers:
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    ...
"""