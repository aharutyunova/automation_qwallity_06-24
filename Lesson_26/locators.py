from selenium.webdriver.common.by import By

# Locators
btn_alert_loc = (By.XPATH, "//input[@id='alertbtn']")
btn_hide_loc = (By.XPATH, "//input[@id='hide-textbox']")
inp_hide_loc = (By.XPATH, "//input[@id='displayed-text']")
btn_mous_loc = (By.XPATH, "//button[@id='mousehover']")
top_option_loc = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
footer_text_loc = (By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")
btn_sign_in_loc = (By.XPATH, "//a[@href='/login']")
email_fld_loc = (By.XPATH, "//input[@placeholder='Email Address']")
pass_fld_loc = (By.XPATH, "//input[@id='login-password']")
btn_login_loc = (By.XPATH, "//button[@id='login']")
msg_valid_loc = (By.XPATH, "//span[@id='incorrectdetails']")
fld_search_loc = (By.XPATH, "//input[@id='id-search-field']")
btn_search_loc = (By.XPATH, "//button[@id='submit']")
results_loc = (By.XPATH, '//div[@id="content"]//li')
