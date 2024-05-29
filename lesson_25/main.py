from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 1
driver = webdriver.Chrome()


# 2
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# 3
btn_alert_loc = (By.XPATH, "//input[@id='alertbtn']")
btn_alert = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(btn_alert_loc)
)
# 4
btn_alert.click()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

# 5 
hide_btn_loc = (By.XPATH, "//input[@id='hide-textbox']")
hide_inp_loc = (By.XPATH, "//input[@id='displayed-text']")

hide_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(hide_btn_loc)
)
hide_btn.click()
print("Clickable")

WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located(hide_inp_loc)
)
print("The input box is successfully hidden.")

# 8
footer_loc = (By.XPATH, "//div[contains(@class,'FooterBlock')]//p")
footer = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(footer_loc)
)
actions = ActionChains(driver)
actions.move_to_element(footer).perform()

footer_text = footer.text
print("Footer text:", footer_text)

# 9
sign_in_btn_loc = (By.XPATH, "//a[@class='navbar-link fedora-navbar-link']")
sign_in_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(sign_in_btn_loc)
)
sign_in_btn.click()
print("Sign In button clicked.")

driver.quit()

# Anna - footer locator, didn't find, try this one //div[contains(@class,'FooterBlock')]//p
# Sign in button not found by your locator in line 53
# Actions generally correct, only you didn't use logging to keep text, messages etc