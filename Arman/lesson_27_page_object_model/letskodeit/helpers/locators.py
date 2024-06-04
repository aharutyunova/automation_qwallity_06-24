from selenium.webdriver.common.by import By

from Arman.lesson_27_page_object_model.letskodeit.helpers.driver import driver

element = driver.find_element(By.XPATH, '//*[@id="alertbtn"]')
hide_button = driver.find_element(By.XPATH, "//*[@id='hide-textbox']")
hide_input_field_xpath = driver.find_element(By.XPATH, "//*[@id='displayed-text']")
footer_block = driver.find_element(By.XPATH, "//*[@id='page']/div[3]")
footer_text = driver.find_element(By.XPATH, "//*[@id='page']/div[3]/div/div/div[1]/div/div[1]/p")
sign_in = driver.find_element(By.XPATH, "//*[@id='navbar-inverse-collapse']/div/div/a")
email_address = driver.find_element(By.XPATH, "//*[@id='email']")
password = driver.find_element(By.XPATH, "//*[@id='login-password']")
login_button = driver.find_element(By.XPATH, "//*[@id='login']")
error_validation = driver.find_element(By.XPATH, "//*[@id='incorrectdetails']")
search_input_field = driver.find_element(By.XPATH, "//*[@id='id-search-field']")
go_button = driver.find_element(By.XPATH, "//*[@id='submit']")
li_elements = driver.find_elements(By.XPATH,
                                   '//ul/li[p[contains(translate(text(), "AUTOMATION", "automation"), "automation")]]')
