from selenium import webdriver
from selenium.webdriver.common.by import By
from config import config_data
import lib

# Locators
lnk_all_course = (By.XPATH, "//a[text()='ALL COURSES']")
element_select = (By.XPATH, "//label[text()='Category']//following-sibling::select")
course_list = (By.XPATH, "//div[@id='course-list']//div[@class='zen-course-list']")
course_price = (By.XPATH, "//span[contains(@class,'zen-course-price')]")
course_title = (By.XPATH, "//div[contains(@class,'zen-course-title')]/h4")
footer = (By.XPATH, "//*[contains(text(), '2024')]")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(config_data['url'])


lib.click_on_element(lnk_all_course, driver)
lib.move_to_element(footer, driver)
# Get all course titles and prices in dictionary courses_dict
courses_dict = {}
prices = lib.get_elements(course_price, driver)
titles = lib.get_elements(course_title, driver)
for i in range(len(prices)):
    courses_dict[titles[i].text] = int(prices[i].text.split('$')[1])
max_key = max(courses_dict, key=courses_dict.get)
print(max_key)
