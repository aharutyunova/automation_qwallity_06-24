from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
import os
import time

script_directory = os.path.dirname(os.path.abspath(__file__))
log_file = 'my_log.log'
log_file_path = os.path.join(script_directory, log_file)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file_path,
    filemode='w+',
    encoding='utf-8'
)

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    logging.info("Navigated to letskodeit.com")

    wait = WebDriverWait(driver, 10)

    # Click the Alert button
    alert_button = wait.until(EC.element_to_be_clickable((By.ID, 'alertbtn')))
    alert_button.click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    logging.info(f'Alert text: {alert_text}')
    alert.accept()
    # Verify the element is hidden
    hide_button = driver.find_element(By.ID, 'hide-textbox')
    hide_button.click()
    element_to_hide = driver.find_element(By.ID, 'displayed-text')
    is_hidden = wait.until(EC.invisibility_of_element_located((By.ID, 'displayed-text')))
    logging.info(f'Element hidden: {is_hidden}')
    # Scroll and click to the Mouse Hover button and Click on Top option
    mouse_hover_button = driver.find_element(By.ID, 'mousehover')
    driver.execute_script("arguments[0].scrollIntoView();", mouse_hover_button)
    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover_button).perform()
    top_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")))
    top_option.click()
    # Go to the footer and log footer text.
    footer = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", footer)
    actions.move_to_element(footer).perform()
    footer_text = footer.text
    logging.info(f'Footer text: {footer_text}')
    # Click on the Sign In button.
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    sign_in_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sign In']")))
    logging.info(f'Sign In button is visible: {sign_in_button.is_displayed()}')
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign In']")))
    logging.info(f'Sign In button is clickable: {sign_in_button.is_enabled()}')
    sign_in_button.click()
    logging.info('Clicked on Sign In button')
    # Fill the fields with incorrect email or password and click the LogIn button.
    email_address = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
    email_address.send_keys("testqatest@gmail.com")
    password = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-password']")))
    password.send_keys("test.123")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login']")))
    login_button.click()
    # Get validation message and log it.
    wait.until(EC.visibility_of_element_located((By.ID, "incorrectdetails")))
    validation_error = driver.find_element(By.ID, "incorrectdetails")
    logging.info(f'Validation error message: {validation_error.text}')

    # Open a new tab, switch to the new tab, and get https://www.python.org/ on the second tab.
    driver.execute_script("window.open('https://www.python.org', '_blank');")
    driver.switch_to.window(driver.window_handles[1])

    # Search the 'Automation' word.
    search_input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='id-search-field']")))
    search_input_field.send_keys("Automation")
    go_button = driver.find_element(By.XPATH, "//*[@id='submit']")
    go_button.click()

    # Wait for search results to load and count the occurrences of 'Automation'.
    search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='list-recent-events menu']/li")))
    automation_count = sum("Automation" in result.text for result in search_results)
    logging.info(f'Number of automation mentions: {automation_count}')

    driver.switch_to.window(driver.window_handles[0])

except Exception as e:
    logging.error("Error occurred: %s", e)

finally:
    driver.quit()

# Anna - steps are correct, only for get autonation result in python.org you should get count of all found result, not only with Automation text
# And I expect you will solve this task using functions and modules