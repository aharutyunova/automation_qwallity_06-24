import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from pytest_auto_am.conftest import driver


def test_search_mazda(driver):
    # Navigate to the auto.am website
    driver.get("https://auto.am")

    # Find the search box element and clear any existing text
    search_box = driver.find_element(By.XPATH, '//*[@id="searchInp-small"]')
    search_box.clear()

    # Enter 'Mazda' into the search box
    search_box.send_keys("Mazda")

    # Wait for 5 seconds to ensure the search results load
    time.sleep(5)

    # Submit the search by pressing the Enter key
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load using WebDriverWait
    wait = WebDriverWait(driver, 5)
    try:
        results = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search-result"]')))
    except TimeoutException:
        print("TimeoutException: No elements found with class name 'car-list-item'")
        raise

    # Print the number of results found
    print(f"Found {len(results)} results.")

    # Check that results are not "Null"
    assert len(results) > 0, "No results found for 'Mazda'"


# Anna mainly logic is correct, I could run test with pytest command
#  But there are some notes
# 1. In condftest.py gile, for selenium 4 no need to import from webdriver_manager.chrome import ChromeDriverManager
# You should initialize driver like we did it without pytest
# 2. Conftest.py file and fixtures from that file are accessable without import, so no need import driver from conftest here
# 3. You didn't use Page object model