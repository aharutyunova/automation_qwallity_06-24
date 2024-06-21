import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Set up the Chrome WebDriver using ChromeDriverManager to handle the installation
    driver = webdriver.Chrome()
    # Yield the driver to the test function
    yield driver
    # Quit the driver after the test finishes to clean up resources
    driver.quit()
