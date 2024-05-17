from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the ChromeDriver with the service
driver = webdriver.Chrome()

# Store Google Chrome and Mozilla Firefox web drivers in the drivers list
drivers = [webdriver.Chrome(), webdriver.Firefox()]

# Run test on each browser
for driver in drivers:
    try:
        # Get application base url
        driver.get("https://www.python.org/")

        # Maximize browser window
        driver.maximize_window()

        # Store search input field id in the search variable
        search = driver.find_element(By.ID, "id-search-field")

        # Fill search input field with data
        search.send_keys("bla bla")

        # Get Log In button XPath and store in the email variable
        go_button = driver.find_element(By.ID, "submit")

        # Click on the Go button
        go_button.click()

        # Store no result store text Xpath in the no_results_found variable
        no_results_found = driver.find_element(By.XPATH, "//*[@id='content']/div/section/form/ul/p")

        # Check search result text matches with expected text
        assert no_results_found.text == "No results found.", "Fail: 'No results found.' text not showed"

        driver.close()

        print(f"Pass: Test passed successfully for {driver.name}.")
    except Exception as error:
        print(error)
