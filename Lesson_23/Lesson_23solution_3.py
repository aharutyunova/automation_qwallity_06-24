from selenium import webdriver
from selenium.webdriver.common.by import By


xPath_dict = {
    "rbtn_benz": "//*[@id='benzradio']",
    "chkbx": "//*[@id='hondacheck']",
    "sw_tab_open": "//*[@id='opentab']",
    "m_select": "//option[@value='orange' or @value='peach']",
    "el_displ_show": "//*[@id='show-textbox']",
    "hide_show": "//*[@id='displayed-text']",
    "name": "//*[@id='enter-name']",
    "mouse_hov": "//*[@id='mouse-hover-example-div']/div/fieldset/legend",
    "web_table": "//td[contains(text(), 'Python Programming Language')]"
}


driver = webdriver.Chrome()
driver.get('https://www.letskodeit.com/practice')

total_count = 0

for key, xpath in xPath_dict.items():
    elements = driver.find_elements(By.XPATH, xpath)
    element_count = len(elements)
    total_count += element_count

print("Total elements count is: ", total_count)

driver.close()
driver.quit()
