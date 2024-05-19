# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     filename='out.log',
#     filemode='w+',
#     encoding='utf-8'
# )

# browsers = ["Firefox"]

# login_success = False

# for browser in browsers:
#     try:
#         if browser == "Chrome":
#             driver = webdriver.Chrome()
#         elif browser == "Firefox":
#             driver = webdriver.Firefox()

#         driver.maximize_window()

#         driver.get("http://www.facebook.com")

#         username = driver.find_element(By.XPATH, "//input[@id='email']")
#         password = driver.find_element(By.XPATH, "//input[@id='pass']")
#         submit = driver.find_element(By.XPATH, "//button[@name='login']")

#         username.send_keys("you@gmail.com")
#         password.send_keys("your_password")

#         submit.click()

#         time.sleep(5)

#         if "login" not in driver.current_url:
#             login_success = True
#             logging.info(f"Login successful using {browser}")
#             break

#     except Exception as e:
#         logging.error(f"An error occurred while trying {browser}: {str(e)}")
#     finally:
#         if not login_success:
#             try:
#                 driver.quit()
#             except:
#                 pass

# if not login_success:
#     logging.error("Login unsuccessful in all browsers. Please check the app or credentials.")

# Anna - everything is good, only in case you check not login_success logging.error, in your case you never login with wrong creds,
# so your login_success always false
# And one more note, quite driver in all cases driver is open, in funally block you should write if driver: driver.quite()

# # 2. case

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='out.log',
    filemode='w+',
    encoding='utf-8'
)

search_term = "bla bla"

search_field_xpath = "//*[@id='id-search-field']"
search_results_xpath = "//*[@id='content']/div/section/form/ul/p"

browsers = ["Chrome", "Firefox"]

success = False

for browser in browsers:
    try:
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Firefox":
            driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get("https://www.python.org/")

        search_field = driver.find_element(By.XPATH, search_field_xpath)
        search_field.send_keys(search_term)

        search_field.submit()

        time.sleep(5)

        search_results = driver.find_element(By.XPATH, search_results_xpath).text
        if search_results == "No results found.":
            logging.info(f"Search test passed using {browser}")
        else:
            logging.error(f"Search test failed using {browser}: Unexpected search results")

        success = True
        break 

    except Exception as e:
        logging.error(f"An error occurred while trying {browser}: {str(e)}")
    finally:
        if not success:
            try:
                driver.quit()
            except:
                pass

if not success:
    logging.error("Search test unsuccessful in all browsers.")

# Anna - in line 112 when you write break, your loop is finished, and second driver doesn't open
# Mainly good solution, pay attention on my notes

# And please for each lesson add folder with that lesson number, and inside that folder add homework's files
