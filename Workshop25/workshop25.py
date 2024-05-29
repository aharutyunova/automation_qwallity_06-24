import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging


logging.basicConfig(
    level=logging.INFO,
    filename='logs.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
driver = webdriver.Chrome()

driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Alert button
btn_alert_loc = (By.XPATH, "//input[@id='alertbtn']")
btn_alert_el = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(btn_alert_loc))
btn_alert_el.click()
al = driver.switch_to.alert
logger.info(f"Alert text: {al.text}")
al.accept()
logger.info("Ok button is clicked")

# Hide button
hide_button_loc = (By.ID, "hide-textbox")
hide_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(hide_button_loc)
)
hide_button.click()
logger.info("Hide button is clicked")

# hidden element
input_textbox_loc = (By.ID, "displayed-text")
hidden_input_textbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(input_textbox_loc)
)
assert "display: none;" in hidden_input_textbox.get_attribute("style"), "Element is not hidden"
logger.info("Element is hidden successfully")

# Scroll to the Mouse Hover button and its actions
mouse_hover_button_loc = (By.ID, "mousehover")
mouse_hover_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(mouse_hover_button_loc)
)
driver.execute_script("arguments[0].scrollIntoView(true);", mouse_hover_button)

actions = ActionChains(driver)
actions.move_to_element(mouse_hover_button).perform()
logger.info("Hovered over the Mouse Hover button")

# Locate and click the "Top" option
top_option_loc = (By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
top_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(top_option_loc)
)
top_option.click()
logger.info("Top option is clicked")

# Footer text logging
footer_text_loc = (By.XPATH, "//*[@id='page']/div[3]/div/div/div[1]/div/div[1]/p")
footer_text_el = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(footer_text_loc))
driver.execute_script("arguments[0].scrollIntoView(true);", footer_text_el)
logger.info("Page is scrolled to the footer")
footer_text = footer_text_el.text
logger.info(f"Footer text: {footer_text}")

# scrolling to the very top of the page
driver.execute_script("window.scrollTo(0, 0);")
logger.info("Page is scrolled to the top")

# Sign In button and its actions
btn_signin_loc = (By.XPATH, "//*[@id='navbar-inverse-collapse']/div/div/a")
btn_signin_el = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(btn_signin_loc))
btn_signin_el.click()  # Click the Sign In button element
logger.info("Sign In button is clicked")
time.sleep(4)

# Switching to Log in page
driver.switch_to.window(driver.window_handles[-1])

# Filling incorrect email
email_field_loc = (By.ID, "email")
email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(email_field_loc))
email_field.send_keys("incorrect@email.com")
logger.info("Incorrect email is filled")
time.sleep(5)

# Filling incorrect password
password_field_loc = (By.XPATH, "//*[@id='login-password']")
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(password_field_loc))
password_field.send_keys("incorrectpassword")
logger.info("Incorrect password is filled")
time.sleep(2)

# Clicking in Login button
login_button_loc = (By.XPATH, "//*[@id='login']")
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_button_loc))
login_button.click()
time.sleep(2)
logger.info("LogIn button is clicked")

# Validation message
validation_msg_loc = (By.ID, "incorrectdetails")
validation_msg = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(validation_msg_loc)
)
validation_text = validation_msg.text.strip()
logger.info(f"Validation message: {validation_text}")

# Opening new tab
driver.execute_script("window.open('', '_blank');")
driver.switch_to.window(driver.window_handles[-1])
logger.info("Successfully switched to the python tab")
driver.get("https://www.python.org/")
logger.info(driver.title)

# searching "Automation" word
search_box_loc = (By.ID, "id-search-field")
search_box_el = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(search_box_loc))
search_box_el.send_keys("Automation")
search_box_el.send_keys(Keys.RETURN)

# finding results
results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list-recent-events "
                                                                                                "> li")))
num_results = len(results)
logger.info(f"Number of search results on the first page: {num_results}")

# switching to the first window
driver.switch_to.window(driver.window_handles[0])
logger.info(driver.title)

# Closing all opened tabs
driver.quit()

# Here I used simple commands
# Concerning lines 77-87 in my computer, after running the code, I need to click on "x" button
# of the notification about Chrome and when scrolling to Sign in button, I need a little scroll up
# so that Sign in button could be visible and clickable, and the system could continue to running the code
# Anna jan if you have some info how to solve such problems please, tell us about it in our next lesson
# I am writting it here in order not to forget to remind you about it in our next lesson :D