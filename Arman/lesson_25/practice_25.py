from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize the WebDriver (make sure to specify the path to your WebDriver executable)
driver = webdriver.Chrome()

# Set an implicit wait of 10 seconds
driver.implicitly_wait(10)

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

except NoSuchElementException:
    print("Element not found within the given time")
except TimeoutException:
    print("Alert not found within the given time")
except Exception as e:
    print(f"An error occurred: {e}")

hide_button = driver.find_element(By.XPATH, "//*[@id='hide-textbox']")

hide_input_field_xpath = driver.find_element(By.XPATH, "//*[@id='displayed-text']")

hide_button.click()

hidden_style = hide_input_field_xpath.get_attribute('style')

if "display: none;" in hidden_style:
    print("Hide/Show input field hidden")
else:
    print("Hide/Show input field show")

hover_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Mouse Hover')]")
# Create an ActionChains object
hover_button.click()

action = ActionChains(driver)
# Scroll to the "Mouse Hover" button
driver.execute_script("arguments[0].scrollIntoView(true);", hover_button)
# Perform mouse hover action on the "Mouse Hover" button
action.move_to_element(hover_button).perform()
# Find and click on the "Top" option
top_option = driver.find_element(By.XPATH, "//div[@class='dropdown-menu']/a[contains(text(), 'Top')]")
top_option.click()

# Close the browser
driver.quit()
