import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w+',
    encoding='utf-8'
)

# Initialize the WebDriver (make sure to specify the path to your WebDriver executable)
driver = webdriver.Chrome()

driver.maximize_window()

# Navigate to a website
driver.get('https://www.letskodeit.com/home')

all_courses = (By.XPATH, '//*[@id="navbar-inverse-collapse"]/ul/li[2]/a')

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(all_courses))

element.click()

action = ActionChains(driver)

footer = driver.find_element(By.XPATH, '//*[@class="small dynamic-text jqCopyRight"]')

driver.execute_script("arguments[0].scrollIntoView(true);", footer)

all_courses_block = driver.find_elements(By.XPATH, "//*[@class='zen-course-price dynamic-text']")

prices = []
for price in all_courses_block:
    prices.append(price.text)

# Initialize the result list
result = []
for number in prices:
    # Remove the dollar sign and convert to an integer
    cleaned_number = number.replace("$", "")
    result_number = int(cleaned_number)
    result.append(result_number)

# Print the result list
print("Complete Test Automation Bundle")
print(f"Maximum price number: ${max(result)}")
