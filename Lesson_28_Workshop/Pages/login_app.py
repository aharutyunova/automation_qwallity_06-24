from selenium.webdriver.common.by import By

# Locators for Login page.
username_field = (By.ID, 'username')
password_field = (By.ID, 'password-field')
login_button = (By.XPATH, '//button[@type="submit"]')