"""
Navigate to "http://www.uitestingplayground.com/"

Go to Visibility, click the Hide button. Check in your program that buttons are hidden.
Go to Progress Bar, click the Start button, then stop it.  Print Duration.
Go to Text Input, enter any text, click the button and check if the button text is the same as the entered text.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Progress bar url
driver.get("http://www.uitestingplayground.com/progressbar")

start_button = driver.find_element(By.XPATH, "//*[@id='startButton']")
stop_button = driver.find_element(By.XPATH, "//*[@id='stopButton']")
start_button.click()
stop_button.click() 


# Task 3: Text Input - Enter Text, Check Button Text
text_input_section = driver.find_element_by_xpath(By.XPATH, '//*[@id="newButtonName"]')
text_input_section.click()

text_input = driver.find_element_by_id(By.XPATH, '//*[@id="updatingButton"]')
text_input.send_keys("Test Text")


same_text(text, same_text_button)
driver.quit()