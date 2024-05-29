from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
driver.back()
driver.forward()
browser_title = driver.title
curr_url = driver.current_url
driver.refresh()

# SEND KEYS
inp_field = driver.find_element(By.XPATH, "//input[@id='name' and @placeholder='Enter Your Name']")
inp_field.send_keys('Anna')
inp_field.clear()

# GET TEXT
pract_page = driver.find_element(By.XPATH, "//h1[text()='Practice Page']")
el_text = pract_page.text

# CLICK 
btn_show = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
btn_show.click()

# GET ATTR
show_hide = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
show_attr = show_hide.get_attribute('style')

# IS_ENABLED/DISABLED
btn_disable = driver.find_element(By.XPATH, "//input[@id='disabled-button']")
btn_disable.click()
d_field = driver.find_element(By.XPATH, "//input[@id='enabled-example-input']")
is_dis = d_field.is_enabled()

# SELECT_OPTION
sel_el = driver.find_element(By.XPATH, "//select[@id='carselect']")
ddl = Select(sel_el)
e_1 = ddl.select_by_index(0)
e_2 = ddl.select_by_value('benz')
e_3 = ddl.select_by_visible_text('Honda')

# SAVE SCREENSHOT
driver.save_screenshot("scrn.png")

# OPEN NEW WINDOW
driver.execute_script("window.open('')")
before = driver.window_handles[0]
after = driver.window_handles[-1]
driver.switch_to.window(after)
driver.get("https://www.python.org/")
print(driver.title)
driver.close()
driver.switch_to.window(before)
print(driver.title)


# ACTIONS CHAIN
el = driver.find_element(By.XPATH, "//legend[text()='iFrame Example']")

actions = ActionChains(driver)
actions.move_to_element(el).perform()
print("test")
