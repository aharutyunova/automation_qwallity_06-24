from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging
import os
import time


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

log_file_path = os.path.join(CURRENT_DIR, 'Lesson_25_log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file_path,
    filemode='w+',
    encoding='utf-8'
)


driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.letskodeit.com/practice')

# 3. Click to open the Alert popup
# 4. Get text from the popup and log it
btn_alert = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, '//*[@id="alertbtn"]')))
btn_alert.click()

alrt = driver.switch_to.alert
logging.info(alrt.text)
alrt.accept()


# 5. Locate the following element, hide it, check element is hidden
hidden_el = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, '//*[@id="hide-textbox"]')))
hidden_el.click()

inp_field = driver.find_element(By.XPATH, '//*[@id="displayed-text"]')
show_attr = inp_field.get_attribute('style')
assert 'display: none' in show_attr, \
    "Failed - input field should be hidden"
logging.info('Pass - input field is hidden')


# 7. Scroll and click to the Mouse Hover button
# and Click on Top option to go to the top of screen
btn_mouse_hover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, '//*[@id="mousehover"]')))
driver.execute_script("arguments[0].scrollIntoView();", btn_mouse_hover)
btn_mouse_hover.click()

btn_top_in_mouse_hover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, '//*[@class="mouse-hover-content"]/a')))
btn_top_in_mouse_hover.click()


# 8. Go to the footer and log footer text
txt_footer = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, '//p[@class="small dynamic-text jqCopyRight"]')))
driver.execute_script("arguments[0].scrollIntoView();", txt_footer)
logging.info(txt_footer.text)


# 9. Click on the Sign In button
time.sleep(2)
btn_sign_in = driver.find_element(
    By.XPATH, '//*[@id="navbar-inverse-collapse"]/div')
btn_sign_in.click()

# 10. Fill the fields with incorrect email
# or password and click the LogIn button (See in the Picture)
inp_email = driver.find_element(By.XPATH, '//*[@id="email"]')
inp_email.send_keys('aaa@gmail.com')
inp_pass = driver.find_element(By.XPATH, '//*[@id="login-password"]')
inp_pass.send_keys('jfcgvjj')
time.sleep(1)
btn_login = driver.find_element(By.XPATH, '//*[@id="login"]')
btn_login.click()
time.sleep(1)
msg_val_login = driver.find_element(By.XPATH, '//span[@id="incorrectdetails"]')
logging.info(msg_val_login.text)


# 12. Open a new tab, switch to the new tab
# 13. Get https://www.python.org/ on the second tab
driver.execute_script("window.open('');")
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
driver.get('https://www.python.org/')


# 14. Search the 'Automation’ word
inp_search = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((
        By.XPATH, '//*[@id="id-search-field"]')))
inp_search.send_keys('Automation')
inp_search.send_keys(Keys.ENTER)

# 15. Write in the log file how many results is found on the first page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
result_list = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/form/ul')
# li_elements = result_list.find_elements(By.TAG_NAME, 'li')
li_elements = result_list.find_elements(
    By.XPATH, '//*[@id="content"]/div/section/form/ul/li')
li_count = len(li_elements)
logging.info("Search result count: " + str(li_count))

# 16. Come back to the first tab
driver.switch_to.window(all_windows[0])

# input("Press any ke to continue...")

# 17. Close all opened tabs
driver.quit()

# Anna jan please also check my solution for Lesson 24 if you have time

# Anna - actions are correct, but I would like you create functions working with elements and solve task with that fucntions
# Homework 24 is checked