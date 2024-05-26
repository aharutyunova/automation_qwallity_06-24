from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import os

Cur_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(Cur_dir, 'my_log_lesson_22')

logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file_path,
                    filemode='w+',
                    encoding='utf-8')

browsers = ['Chrome', 'Firefox']
# for browser in browsers:
#     if browser == 'Chrome':
#         driver = webdriver.Chrome()
#         logging.info(f"This browser {browser} is supported")
#     elif browser == 'Firefox':
#         driver = webdriver.Firefox()
#         logging.info(f"This browser {browser} is supported")
#     else:
#         logging.error("Browser is not available")

for browser in browsers:
    driver = getattr(webdriver, browser, None)()
    logging.info(f"This browser {browser} is supported")


    def func_test():
        try:
            driver.get("https://www.python.org")
            driver.maximize_window()
            search_text = driver.find_element(By.ID, "id-search-field")
            search_text.send_keys("bla bla")
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()
            result = driver.find_element(By.XPATH, "//*[@id='content']/div/section/form/ul/p")
            assert result.text == "No results found."
            logging.info("Test is passed")
            driver.close()
            print("Test passed successfully")
        except Exception as e:
            print(e)

    func_test()

    #Anna jan, but I did not understand why code runs so long and so slowly. Maybe there is  more optimal option?

# Armine jan on my side code run was not slowly. 
# But run code on different browsers, you can use solution, which is Lusine implemented
# I added it in line 28
# It will help you avoid write so many if else, and also will increase performance

# Solution is correct :)
"""
Step 1) Open browser
Step 2) Navigate to python.org
Step 3) Search "bla bla" text
Step 4) Click on Go button
Step 5) Close driver
Step 6 ) Check Result will be No results found. 


Technical solution
Do the following in all type of browsers(Chrome and Firefox). Make for loop for sequence.
Handle exceptions
Use Logging
"""