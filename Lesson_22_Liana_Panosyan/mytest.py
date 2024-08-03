from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
import os
print("Sample test case started:")

script_directory = os.path.dirname(os.path.abspath(__file__))
log_file = 'test_log.log'
log_file_path = os.path.join(script_directory, log_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file_path,
    filemode='w+',
    encoding='utf-8'
)


def my_func(active_driver):
    try:
        active_driver.get("https://www.python.org/")
        time.sleep(1)
        active_driver.maximize_window()
        time.sleep(1)
        active_driver.find_element(By.NAME, "q").send_keys("bla bla")
        time.sleep(1)
        active_driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
        search_result = active_driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul/p').text
        if (search_result == "No results found."):
            print("The test case passed:")
            time.sleep(1)
            active_driver.close()
        else:
            active_driver.close()
            logging.error("The test case failed:")
    except Exception as error:
        print(error)


my_func(webdriver.Chrome())
my_func(webdriver.Firefox())


# Anna - Good job, everything almost correct, will add several notes
#  - For logging use INFO mode instead DEBUG, it will be more readable
# All messages add to log instead of print
#  - diver.close() you could write in finally block, so even something went wrong, driver.close() will work