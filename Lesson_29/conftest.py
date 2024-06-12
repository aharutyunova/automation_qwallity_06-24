import pytest
from selenium import webdriver
from Helpers.logging_config import configure_logging


@pytest.fixture(scope="session")
def driver():
    configure_logging()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()