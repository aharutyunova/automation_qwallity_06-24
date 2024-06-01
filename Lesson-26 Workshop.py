from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.letskodeit.com')
all_courses = driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/ul/li[2]/a')
all_courses.click()


element = driver.find_element(By.XPATH, '//*[@id="page"]/div[3]/div/div/div[1]/div/div[2]/ul/li[5]/a')
action = ActionChains(driver)
action.move_to_element(element).perform()


# price = driver.find_element(By.XPATH, '//*[@id="course-list"]/div[2]/div/a/div[1]/div[2]/div/span[2]')
# val = price.get_attribute()
# print("price = ", val)


# p = driver.find_elements(By.TAG_NAME, "span")
p = driver.find_elements(By.XPATH, '//span[@class="zen-course-price dynamic-text"]')

for el in p:
    x = el.text.split("$")[1]
    print("p", x)


# print(len(p))
