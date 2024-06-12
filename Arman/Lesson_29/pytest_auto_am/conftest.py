import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Set up the Chrome WebDriver using ChromeDriverManager to handle the installation
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Yield the driver to the test function
    yield driver
    # Quit the driver after the test finishes to clean up resources
    driver.quit()
