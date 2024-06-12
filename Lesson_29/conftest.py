import pytest
from selenium import webdriver
from Helpers.logging_config import configure_logging
import logging

@pytest.fixture(scope="session")
def driver():
    configure_logging()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='mylog.log'
    )
