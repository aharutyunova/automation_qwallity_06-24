# Search

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

#  Search 2

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


# 3. find element

element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

from selenium.webdriver.support.ui import Select

select = Select(driver.find_element(By.NAME, 'name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)


driver.find_element(By.ID, "submit").click()


# 4 Switch to another tab
driver.switch_to.window("windowName")

# 5 switch to alert popup
alert = driver.switch_to.alert


# browser back and forward
driver.forward()
driver.back()

# wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()


from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))


from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()


# close() and quit

from selenium import webdriver
import time

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

# Open the first webpage
driver.get("https://www.example.com")
time.sleep(2)  # Just for demonstration, wait for 2 seconds

# Open a new window or tab
driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")
time.sleep(2)  # Wait for 2 seconds

# Switch to the new window/tab
driver.switch_to.window(driver.window_handles[1])
print(f"Current URL (second tab): {driver.current_url}")

# Close the current window (second tab)
driver.close()
time.sleep(2)  # Wait for 2 seconds

# Switch back to the first window/tab
driver.switch_to.window(driver.window_handles[0])
print(f"Current URL (first tab): {driver.current_url}")

# Close the first window and end the session
driver.quit()
