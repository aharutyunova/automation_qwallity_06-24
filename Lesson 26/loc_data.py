from selenium.webdriver.common.by import By # Import the By class for locating elements with Selenium

# Define locators
btn_alert_loc = (By.ID, 'alertbtn')
btn_hide_loc = (By.ID, 'hide-textbox')
inp_hide_loc = (By.ID, 'displayed-text')
btn_mouse_loc = (By.ID, 'mousehover')
top_option_loc = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
footer_txt_loc = (By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")
btn_sign_in_loc = (By.XPATH, "//a[@href='/login']")
email_fld_loc = (By.ID, "email")
password_fld_loc = (By.ID, "login-password")
btn_login_loc = (By.ID, "login")
msg_valid_loc = (By.ID, 'incorrectdetails')
fld_search_loc = (By.ID, "id-search-field")
btn_search_loc = (By.ID, "submit")
results_loc = (By.XPATH, '//div[@id="content"]//li')