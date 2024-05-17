from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up the ChromeDriver service
chrome_driver_path = ChromeDriverManager().install()
service = Service(chrome_driver_path)

# Initialize the ChromeDriver with the service
driver = webdriver.Chrome(service=service)

# Get application base url
driver.get("https://www.python.org/")

# Maximize browser window
driver.maximize_window()

# Store search input field id in the search variable
search = driver.find_element(By.ID, "id-search-field")

# Fill search input field with data
search.send_keys("bla bla")

# Get Log In button XPath and store in the email variable
go_button = driver.find_element(By.ID, "submit")

# Click on the Go button
go_button.click()

# Store no result store text Xpath in the no_results_found variable
no_results_found = driver.find_element(By.XPATH, "//*[@id='content']/div/section/form/ul/p")

# Check search result text matches with expected text
assert no_results_found.text == "No result found.", "Not displayed No result found."

driver.close()
print("Test is finished")
