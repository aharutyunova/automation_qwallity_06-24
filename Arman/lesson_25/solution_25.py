import logging

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from modules import check_hidden

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w+',
    encoding='utf-8'
)

"""
# 1. Open Chrome browser
# 2. Navigate to https://www.letskodeit.com/practice
# 3. Click to open the Alert popup
"""

# Initialize the WebDriver (make sure to specify the path to your WebDriver executable)
driver = webdriver.Chrome()

# Set an implicit wait of 10 seconds
driver.implicitly_wait(5)

# Navigate to a website
driver.get('https://www.letskodeit.com/practice')

try:
    # Attempt to find the element with id 'alert_button' and click it
    element = driver.find_element(By.XPATH, '//*[@id="alertbtn"]')
    element.click()

    # Attempt to switch to the alert
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)

    # Accept the alert (click OK)
    alert.accept()
    print("Alert accepted!")

# except NoSuchElementException:
#     print("Element not found within the given time")
# except TimeoutException:
#     print("Alert not found within the given time")
except Exception as e:
    print(f"An error occurred: {e}")

"""
 4. Get text from the popup and log it
 5. Locate the following element, hide it, check element is hidden
"""

# Hide button XPath
hide_button = driver.find_element(By.XPATH, "//*[@id='hide-textbox']")

# Hide/Show Example input field  XPath
hide_input_field_xpath = driver.find_element(By.XPATH, "//*[@id='displayed-text']")

# Hide button click
hide_button.click()

# Get Hide/Show Example input field style attribute
hidden_style = hide_input_field_xpath.get_attribute('style')

# Check if Hide/Show input field hidden
check_hidden(hidden_style)

# 7. Scroll and click to the Mouse Hover button and Click on Top option to go to the top of screen

# Create an ActionChains object
action = ActionChains(driver)

hover_button = driver.find_element(By.XPATH, "//*[@id='mousehover']")

# Scroll to the "Mouse Hover" button
driver.execute_script("arguments[0].scrollIntoView(true);", hover_button)

# Click on the Mouse Hover button
hover_button.click()

# Set an implicit wait of 10 seconds
driver.implicitly_wait(5)

# Perform mouse hover action on the "Mouse Hover" button
action.move_to_element(hover_button).perform()

# Find and click on the "Top" option
top_option = driver.find_element(By.XPATH, "//a[contains(text(), 'Top')]")
top_option.click()

# 8. Go to the footer and log footer text

# Find the footer element
footer = driver.find_element(By.XPATH, "//*[@id='page']/div[3]")

# Scroll down to the footer element
driver.execute_script("arguments[0].scrollIntoView();", footer)

# Footer text XPath
footer_text = driver.find_element(By.XPATH, "//*[@id='page']/div[3]/div/div/div[1]/div/div[1]/p")

# Print footer text
if footer_text.text:
    logging.info(footer_text.text)
else:
    logging.error("There is no text in the footer")

"""
9. Click on the Sign In button
10. Fill the fields with incorrect email or password and click the LogIn button (See in the Picture)
11. Get validation message and log it
12. Open a new tab, switch to the new tab
13. Get https://www.python.org/ on the second tab
14. Search the 'Automation’ word
15. Write in the log file how many results is found on the first
page
16. Come back to the first tab
17. Close all opened tabs
"""

# Sign in text/button XPath
sign_in = driver.find_element(By.XPATH, "//*[@id='navbar-inverse-collapse']/div/div/a")

#  Click on the Sign-In button
sign_in.click()

# Set an implicit wait of 10 seconds
driver.implicitly_wait(5)

test_email_address = "test@gmail.com"
test_password = "test12345"

# Sign in page Email Address input field XPath
email_address = driver.find_element(By.XPATH, "//*[@id='email']")

# Sign in page Password input field XPath
password = driver.find_element(By.XPATH, "//*[@id='login-password']")

# Sign in page login button XPath
login_button = driver.find_element(By.XPATH, "//*[@id='login']")

email_address.send_keys(test_email_address)
password.send_keys(test_password)

# Click on the login button
login_button.click()

# Set an implicit wait of 10 seconds
driver.implicitly_wait(5)

error_validation = driver.find_element(By.XPATH, "//*[@id='incorrectdetails']")

# Log error validation in the app.log file
logging.info(error_validation.text)

driver.execute_script("window.open('')")

first_tab = driver.window_handles[0]
second_tab = driver.window_handles[1]

# Switch to second tab
driver.switch_to.window(second_tab)

# Progress bar url
driver.get("https://www.python.org/")

# python.org home page search input field XPath
search_input_field = driver.find_element(By.XPATH, "//*[@id='id-search-field']")

search_input_field.send_keys("Automation")

# python.org home page GO button XPath
go_button = driver.find_element(By.XPATH, "//*[@id='submit']")

# Click on the GO button
go_button.click()

# Set an implicit wait of 10 seconds
driver.implicitly_wait(5)

# Find all li elements within the ul element that contain the text "Automation"
li_elements = driver.find_elements(By.XPATH,
                                   '//ul/li[p[contains(translate(text(), "AUTOMATION", "automation"), "automation")]]')

# Count the number of such li elements
automation_count = len(li_elements)

print(f"Count of 'Automation' word after search: {automation_count}")

# Switch to first tab
driver.switch_to.window(first_tab)

# Close the browser
driver.quit()

# Anna - I changed xpath in line 92. And related to other xpaths, try to use minimum components and indexes like
# /a/div[2]/div...etc. sign in button not always visible when click on top, so additional move to element is needed
# for stability If you use implicitly.wait, no need to write it every time, when you one time write
# driver.implicitly_wait(5) it means for all session , before work with any element, driver will wait 5 seconds
# Automation result in python.org is 20, the correct xpath is //ul[@class='list-recent-events menu']/li (line 186)

# Generally commands are correct, need a bit more time and practice
