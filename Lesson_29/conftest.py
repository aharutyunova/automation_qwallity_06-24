import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit() 