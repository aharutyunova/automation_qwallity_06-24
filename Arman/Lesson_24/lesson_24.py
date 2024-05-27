"""
Navigate to "http://www.uitestingplayground.com/"

Go to Visibility, click the Hide button. Check in your program that buttons are hidden.
Go to Progress Bar, click the Start button, then stop it.  Print Duration.
Go to Text Input, enter any text, click the button and check if the button text is the same as the entered text.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from modules import same_text

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

# Visibility page buttons XPath list
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

second_tab = driver.window_handles[0]
third_tab = driver.window_handles[1]

# Switch to Text Progress bar tab
driver.switch_to.window(second_tab)

# Progress bar url
driver.get("http://www.uitestingplayground.com/progressbar")

start_button = driver.find_element(By.XPATH, "//*[@id='startButton']")
stop_button = driver.find_element(By.XPATH, "//*[@id='stopButton']")
start_button.click()
stop_button.click()

# Switch to Text Input tab
driver.switch_to.window(third_tab)

# Text Input url
driver.get("http://www.uitestingplayground.com/textinput")

# Request text for input Playground input field
text = "Test Button"
playground_input = driver.find_element(By.XPATH, '//*[@id="newButtonName"]')
playground_input.send_keys(text)
same_text_button = driver.find_element(By.XPATH, '//*[@id="updatingButton"]')
same_text_button.click()

same_text(text, same_text_button)

# Close all tabs and quit
driver.quit()

# Anna - in line 47 you try handle window with index 2, but you have just 2 active tab 0 and 1, so you get out of range error here
#  I didn't understand how you check that button are hidden for the first task? You get all elements locators and get them in the list,
# But I didn't see checking part, how you verify, that after click on hide, or buttons become hidden

# For second task you didn't get duration
# Last task is correct

# Arman jan I noticed that you try to quickly solve tasks and send.
# Try to spent more time to go deep with the requirements, even you solve task in the first day, don't send it, 
# have a look on the next day be sure everything is correct and then send
   