from selenium.webdriver.common.by import By

# all locators

alert_button = (By.ID, 'alertbtn')
hide_button = (By.ID, 'hide-textbox')
element_to_hide = (By.ID, 'displayed-text')
mouse_hover_button = (By.ID, 'mousehover')
top_option = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
footer = (By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")
sign_in_button = (By.XPATH, "//a[text()='Sign In']")
email_address = (By.XPATH, "//*[@id='email']")
password = (By.XPATH, "//*[@id='login-password']")
login_button = (By.XPATH, "//*[@id='login']")
validation_error = (By.ID, "incorrectdetails")
search_input_field = (By.XPATH, "//*[@id='id-search-field']")
search_result = (By.XPATH, "//ul[@class='list-recent-events menu']/li")
