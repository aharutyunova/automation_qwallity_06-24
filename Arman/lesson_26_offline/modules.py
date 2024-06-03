
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def get_prices(courses_block):
    """Function get courses block prices and return prices list"""
    # Store prices in the list with currency sign
    prices_with_sign = []
    # Store prices in the list without a currency sign
    prices_without_sign = []
    for price in courses_block:
        prices_with_sign.append(price.text)
    for number in prices_with_sign:
        cleaned_number = number.replace("$", "")
        result_number = int(cleaned_number)
        prices_without_sign.append(result_number)
    return prices_without_sign


def scroll_to_footer(browser_driver):
    """Function scroll down to the page footer part"""
    # Initialize ActionChains for performing advanced interactions
    action = ActionChains(browser_driver)
    # Locate the footer element using its XPath
    footer = browser_driver.find_element(By.XPATH, '//*[@class="small dynamic-text jqCopyRight"]')
    return footer
