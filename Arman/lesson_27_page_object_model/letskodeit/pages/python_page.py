from selenium.webdriver.common.by import By

from Arman.lesson_27_page_object_model.letskodeit.helpers.driver import driver

search_input_field = driver.find_element(By.XPATH, "//*[@id='id-search-field']")
go_button = driver.find_element(By.XPATH, "//*[@id='submit']")
li_elements = driver.find_elements(By.XPATH,
                                   '//ul/li[p[contains(translate(text(), "AUTOMATION", "automation"), "automation")]]')
