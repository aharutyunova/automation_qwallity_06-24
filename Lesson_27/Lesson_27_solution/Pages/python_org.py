from Helpers import basic_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging


inp_search_loc = (By.XPATH, '//*[@id="id-search-field"]')
result_list = (By.XPATH, '//*[@id="content"]/div/section/form/ul/li')


def searching_in_Python_org(driver, word):
    try:
        inp_search = basic_page.find_elem_ui(driver, inp_search_loc)
        inp_search.send_keys(word)
        inp_search.send_keys(Keys.ENTER)
    except Exception as e:
        logging.error(f"Error occurred: {e}")


def search_result(driver):
    try:
        elements = basic_page.find_elements(driver, result_list)
        res_count = len(elements)
        logging.info("Search result count: " + str(res_count))
    except Exception as e:
        logging.error(f"Error occurred: {e}")
