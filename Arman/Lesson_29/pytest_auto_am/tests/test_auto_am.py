import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_search_mazda(driver):
    # Step 1: Navigate to the auto.am website
    driver.get("https://auto.am")

    # Step 2: Find the search box element and clear any existing text
    search_box = driver.find_element(By.XPATH, '//*[@id="searchInp-small"]')
    search_box.clear()

    # Step 3: Enter 'Mazda' into the search box
    search_box.send_keys("Mazda")

    # Step 4: Wait for 5 seconds to ensure the search results load
    time.sleep(5)

    # Step 5: Submit the search by pressing the Enter key
    search_box.send_keys(Keys.RETURN)

    # Step 6: Wait for the search results to load using WebDriverWait
    wait = WebDriverWait(driver, 5)
    try:
        results = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search-result"]')))
    except TimeoutException:
        print("TimeoutException: No elements found with class name 'car-list-item'")
        raise

    # Step 7: Print the number of results found
    print(f"Found {len(results)} results.")

    # Step 8: Check that results are not "Null"
    assert len(results) > 0, "No results found for 'Mazda'"
