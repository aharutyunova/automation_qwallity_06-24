import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


try:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    log_file_path = os.path.join(CURRENT_DIR, 'Lesson_22_log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log_file_path,
        filemode='w+',
        encoding='utf-8'
    )
except Exception as e:
    raise ValueError("Error setting up logging: %s", str(e))


browser_list = {1: "Chrome", 2: "Firefox", 3: "Edge"}
search_queries = {
    "bla bla": "No results found",
    "dictionary": "Results found"
}

for browser in browser_list.values():
    try:
        driver = getattr(webdriver, browser, None)()
        if driver is None:
            logging.error(f"Browser '{browser}' is not supported")
            continue

        try:
            driver.maximize_window()
            driver.get("https://www.python.org")

            for query, expected_result in search_queries.items():
                search = driver.find_element(By.ID, "id-search-field")
                search.clear()
                search.send_keys(query)
                button_go = driver.find_element(By.ID, "submit")
                button_go.click()

                try:
                    no_results_message = driver.find_element(
                        By.XPATH, '//*[@id="content"]/div/section/form/ul/p'
                        )
                    if no_results_message.is_displayed():
                        assert expected_result == "No results found", (
                            "Expected 'No results found' but got results for "
                            f"'{query}'"
                        )
                        logging.info(
                            "No results found for query: "
                            f"'{query}' on {browser}"
                            )
                    else:
                        logging.info(
                            f"Results found for query: '{query}' on {browser}"
                            )

                except NoSuchElementException:
                    assert expected_result == "Results found", (
                        "Expected results but got 'No results found' for "
                        f"'{query}'"
                    )
                    logging.info(
                        f"Results found for query: '{query}' on {browser}"
                        )

            logging.info(f"Test completed successfully on {browser}")

        except Exception as e:
            logging.error(
                f"An error occurred while performing actions on {browser}: {e}"
                )
        finally:
            driver.quit()
            logging.info(f"{browser} browser closed.")
    except Exception as e:
        logging.error(
            f"An error occurred while setting up {browser} browser: {e}"
            )

# Anna - good job, especially part with get driver, only you didn't check
# No result Found text exists on the page
# And for logging use INFO instead of DEBUG, it will make log more readable
