# 1. Navigate by the following URL:  https://www.letskodeit.com/practice
# 2. Find effective XPaths  for the elements that are
# highlighted in the screenshot below.
# 3. Print how many elements you found in total.

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")

xpaths_list = [
    "//input[@id='benzradio']",
    "//input[@id='hondacheck']",
    "//a[@id='opentab']",
    "//select[@id='multiple-select-example']/option[@value='orange' or @value='peach']",
    "//input[@id='show-textbox'] | //input[@id='displayed-text']",
    "//div[@id='alert-example-div']//input[@id='name']",
    "//div[@id='mouse-hover-example-div']/div/fieldset/legend[text()='Mouse Hover Example']",
    "//table[@id='product']/tbody/tr/td[@class='course-name'][text() = 'Python Programming Language']"
]

elements_count = 0
for xpath in xpaths_list:
    elements = driver.find_elements(By.XPATH, xpath)
    elements_count += len(elements)

print(f"Total number of elements found: {elements_count}")

driver.close()

# Anna - Everything is correct and good organized, only last 2 xpath could be more optmimal
#  //div[@id='mouse-hover-example-div']//legend[text()='Mouse Hover Example']
# //table[@id='product']//td[text() = 'Python Programming Language']