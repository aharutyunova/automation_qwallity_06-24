
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging

# Configure logging to a file
logging.basicConfig(filename='Log_file.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("https://www.letskodeit.com/practice")
    driver.maximize_window()
    logging.info("Navigated to letskodeit.com/practice page")

    # Step 2: Wait for the "Alert" button to be clickable and click it to open the alert popup
    alert_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'alertbtn'))
    )
    alert_button.click()
    logging.info("Clicked on the Alert button")

    # Step 3: Wait for the alert to be present
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Step 4: Switch to the alert and accept it
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    logging.info(f"Alert accepted with text: {alert_text}")

    # Step 5: Wait for the input text to be present and click the "Hide" button
    input_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'displayed-text'))
    )

    hide_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'hide-textbox'))
    )
    hide_button.click()
    logging.info("Clicked on the Hide button")

    driver.execute_script("arguments[0].style.display = 'none';", input_text)
    logging.info("Hide/Show Example text has been hidden")

    # Check if the element is hidden
    display_style = input_text.value_of_css_property('display')
    assert display_style == 'none', "Element is not hidden"
    logging.info("Element has been hidden")

    # Step 6: Scroll to the Mouse Hover button
    mouse_hover_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'mousehover'))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", mouse_hover_button)
    logging.info("Scrolled to Mouse Hover button")

    # Step 7: Perform mouse hover action and click the 'Top' option
    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover_button).perform()
    logging.info("Performed mouse hover action on Mouse Hover button")

    # Wait for the 'Top' option to be visible and click it
    top_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="mouse-hover-example-div"]/div[1]/fieldset/div/div/a[1]')) 
    )

    top_option.click()
    logging.info("Clicked on the 'Top' option")

    # Step 8: Scroll to the Footer element and log its text
    footer_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[3]'))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)
    logging.info("Scrolled to Footer")
    
    # Get the text content of the footer
    footer_text = footer_element.text
    logging.info(f"Footer displayed with text: {footer_text}")

    # Step 9: Scroll to the Header element
    header_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header5"]/div/nav'))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", header_element)
    logging.info("Scrolled to Header")

    # Step 10: Click on the Sign in button
    sign_in_button = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a'))
    )
    # Use JavaScript to click the element directly
    driver.execute_script("arguments[0].click();", sign_in_button)
    logging.info("Clicked on the Sign in button")

    # Switching to Login page
    driver.switch_to.window(driver.window_handles[-1])

    # Step 11: Fill the email and password fields with incorrect credentials
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("incorrect_email@example.com")
    logging.info("Filled email field with incorrect email")

    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("incorrect_password")
    logging.info("Filled password field with incorrect password")

    # Step 12: Click the Log In button
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    logging.info("Clicked on the Log In button")

    # Step 13: Log the validation message
    validation_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'incorrectdetails'))
    )
    validation_text = validation_message.text
    logging.info(f"Validation message: {validation_text}")

    # Step 14: Open a new tab
    driver.execute_script("window.open('about:blank', '_blank');")
    logging.info("Opened a new tab")

    # Step 15: Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])
    logging.info("Switched to the new tab")

    # Step 16: Open https://www.python.org/ on the second tab
    driver.get("https://www.python.org/")
    logging.info("Opened https://www.python.org/ on the second tab")

    # Step 17: Search for the 'Automation' word
    search_box = driver.find_element(By.ID, "id-search-field")
    search_box.send_keys("Automation")
    logging.info("Searched for the 'Automation' word")
    results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events > li")
    num_results = len(results)
    logging.info(f"Number of search results on the first page: {num_results}")

    # Step 18: Switch back to the first tab
    driver.switch_to.window(driver.window_handles[0])
    logging.info("Switched back to the first tab")

except Exception as e:
    logging.error("Error occurred: %s", e)

finally:
    # Step 19: Close the browser
    driver.quit()
    logging.info("Browser has been closed")


# Please check also lesson 23


        