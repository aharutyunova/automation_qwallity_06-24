import logging

from selenium import webdriver

# Initialize a Google Chrome driver
driver = webdriver.Chrome()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='test.log',
    filemode='w+',
    encoding='utf-8'
)

