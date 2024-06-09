from selenium import webdriver
import config
from logging import configure_logging
from general import Test

def main():
    configure_logging()

    driver = webdriver.Chrome()
    url = config.url
    helper = Test(driver)  # Assuming Test class is the BaseHelper in the provided context

    helper.open_url(url)
    helper.hide_element()
    driver.quit()

if __name__ == "__main__":
    main()
