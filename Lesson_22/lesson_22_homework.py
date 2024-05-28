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
import logging 
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

path = os.getcwd()
full_path = os.path.join(path, 'Lesson_22')
os.chdir(full_path)

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log_Lesson_22.log', 
                    filemode='w+', 
                    encoding='utf-8')

browsers = ['Chrome','Firefox']    

for i in browsers:
    try:
        if i == 'Chrome':
            driver = webdriver.Chrome()
        elif i == 'Firefox':
            driver = webdriver.Firefox()
        else:
             print("No such browser type")
        logging.info(f"{i} browser is opened")
        driver.maximize_window()
        logging.info(f"{i} browser is maximized")
        try:
            driver.get("https://www.python.org/")
            search = driver.find_element(By.ID, 'id-search-field')
            search_text = search.send_keys('bla bla')
            go_btn = driver.find_element(By.ID, 'submit').click()
            result = driver.find_element(By.XPATH, "//ul[@class='list-recent-events menu']")
            error_ = "Expected result isn't 'No results found.'"
            try:
                print(result.text)
                assert result.text == "No results found.", (error_)
                logging.info("assertion passed")
            except AssertionError as err:
                logging.error(f"result assertion error: {err}")
        except Exception as err:
            logging.error(f"browser inside error: {err}")

    except Exception as err:
        logging.error(f"browser opening error: {err}")
    finally:
        driver.quit()
        logging.info(f"{i} browser closed.")