from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://www.letskodeit.com/practice")

element_count = []

benz_radio_button = driver.find_element(By.XPATH, "//input[@id='benzradio']")
benz_radio_button = driver.find_element(By.XPATH, "//*[@id='benzradio']")
benz_radio_button.click()
element_count.append("Benz Radio Button")
time.sleep(2)

honda_checkbox = driver.find_element(By.XPATH, "//input[@id='hondacheck']")
honda_checkbox = driver.find_element(By.XPATH,"//*[@id='hondacheck']")
honda_checkbox.click()
element_count.append("Honda Checkbox")
time.sleep(2)

open_tab_button = driver.find_element(By.XPATH, "//a[@id='opentab']")
open_tab_button.click()
element_count.append("Open Tab Button")
time.sleep(3)

orange_option = driver.find_element(By.XPATH, "//*[@id='multiple-select-example']/option[2]")
orange_option.click()
element_count.append("Orange Option")
time.sleep(2)

peach_option = driver.find_element(By.XPATH, "//*[@id='multiple-select-example']/option[3]")
peach_option.click()
element_count.append("Peach Option")
time.sleep(2)

show_button = driver.find_element(By.XPATH, "//*[@id='show-textbox']")
try:
    show_button.click()
    print('Button is clicked')
    element_count.append("Show Button")
except Exception as ex:
    print("Button wasn't clicked")
displayed_text = driver.find_element(By.XPATH, "//*[@id='displayed-text']")
displayed_text.click()
displayed_text.send_keys('text')
element_count.append("Displayed Text Field")
time.sleep(2)

enter_name_field = driver.find_element(By.XPATH, "//*[@id='name']")
enter_name_field.click()
enter_name_field.send_keys("First name/Last name")
element_count.append("Enter name field")
time.sleep(2)

mouse_hover_example = driver.find_element(By.XPATH, "//*[@id='mouse-hover-example-div']/div[1]/fieldset/legend")
try:
    mouse_hover_example.click()
    print('Mouse Hover Example')
    element_count.append("Mouse Hover Example")
except Exception as ex:
    print("Button wasn't found")
time.sleep(2)

python_programming = driver.find_element(By.XPATH, "//*[@id='product']/tbody/tr[3]/td[2]")
try:
    python_programming.click()
    print('Python Programming Language')
    element_count.append("Python Programming Language")
except Exception as ex:
    print("Element wasn't found")
time.sleep(3)

print(f"Total elements found: {len(element_count)}")

driver.quit()
