from selenium import webdriver
import config
from logging_config import configure_logging
from basic_page import Basic_Helper
from practice import Practice_Page


def test():
    configure_logging()

    driver = webdriver.Chrome()
    url = config.url
    helper = Basic_Helper(driver)
    practice_page = Practice_Page(driver)

    helper.open_url(url)
    practice_page.hide_element()
    driver.quit()


if __name__ == "__main__":
    test()


'''
Anna jan my work is very incomplete.
I spent a lot of time trying to import from different folders,
but could not solve the problem either by creating an
environment or in any other way.
So I took the files out of the folders.
In short, I still have a lot to do on this task (((
Also, I got a little confused and there are things I just wrote,
but I haven't digested them yet.
'''
