"""
Navigate to "http://www.uitestingplayground.com/"

Go to Visibility, click the Hide button. Check in your program that buttons are hidden.
Go to Progress Bar, click the Start button, then stop it.  Print Duration.
Go to Text Input, enter any text, click the button and check if the button text is the same as the entered text.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Visibility bar url
driver.get("http://www.uitestingplayground.com/visibility")

# Visibility page buttons XPath
hide_button = driver.find_element(By.XPATH, "//*[@id='hideButton']")
removed_button = driver.find_element(By.XPATH, "//*[@id='removedButton']")
zero_width_button = driver.find_element(By.XPATH, "//*[@id='zeroWidthButton']")
overlapped_button = driver.find_element(By.XPATH, "//*[@id='overlappedButton']")
opacity_button = driver.find_element(By.XPATH, "//*[@id='transparentButton']")
visibility_hidden_button = driver.find_element(By.XPATH, "//*[@id='invisibleButton']")
display_none_button = driver.find_element(By.XPATH, "//*[@id='notdisplayedButton']")
offscreen_button = driver.find_element(By.XPATH, "//*[@id='offscreenButton']")

hide_button.click()

button_ids = [
    hide_button,
    removed_button,
    zero_width_button,
    overlapped_button,
    opacity_button,
    visibility_hidden_button,
    display_none_button,
    offscreen_button
]

driver.execute_script("window.open('')")
first_tab = driver.window_handles[0]
second_tab = driver.window_handles[1]
third_tab = driver.window_handles[2]
driver.switch_to.window(second_tab)

# Progress bar url
driver.get("http://www.uitestingplayground.com/progressbar")

start_button = driver.find_element(By.XPATH, "//*[@id='startButton']")
stop_button = driver.find_element(By.XPATH, "//*[@id='stopButton']")
start_button.click()
stop_button.click()

driver.switch_to.window(third_tab)

# Text Input url
driver.get("http://www.uitestingplayground.com/textinput")

text = "Test Button"
playground_input = driver.find_element(By.XPATH, '//*[@id="newButtonName"]')
playground_input.send_keys(text)
same_text_button = driver.find_element(By.XPATH, '//*[@id="updatingButton"]')
same_text_button.click()

if text == same_text_button.text:
    print("Text and button texts are same")
else:
    print("Text and button texts are not same!")

driver.quit()
