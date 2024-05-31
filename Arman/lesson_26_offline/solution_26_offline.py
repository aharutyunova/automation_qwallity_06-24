import logging

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from modules import *

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w+',
    encoding='utf-8'
)

# Initialize the Google Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window to full screen
driver.maximize_window()

# Navigate to the specified website
driver.get('https://www.letskodeit.com/home')

# Define the locator for the 'All Courses' link in the navigation bar
all_courses = (By.XPATH, '//*[@id="navbar-inverse-collapse"]/ul/li[2]/a')

# Wait until the 'All Courses' link is present and clickable (max 10 seconds)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(all_courses))

# Click the 'All Courses' link
element.click()

footer = scroll_to_footer(driver)

# Scroll to the footer element to ensure it's in view
driver.execute_script("arguments[0].scrollIntoView(true);", footer)

# Locate all course price elements using their common class name
all_courses_block = driver.find_elements(By.XPATH, "//*[@class='zen-course-price dynamic-text']")

# Extract prices from the located elements using a custom function (assumed to be defined in 'modules')
prices_list = get_prices(all_courses_block)

# Print the maximum price found in the list of prices
print(f"Maximum price number: ${max(prices_list)}")
