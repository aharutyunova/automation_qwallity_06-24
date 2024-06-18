
"""
Navigate to "http://www.uitestingplayground.com/"

Go to Progress Bar, click the Start button, then stop it.  Print Duration.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging
import os
import re

try:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(CURRENT_DIR, 'Lesson_24_log')
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


def extract_duration(result_text):
    match = re.search(r'duration: (\d+)', result_text)
    if match:
        return match.group(1)
    else:
        raise ValueError("Duration not found in result text")


def main():
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.uitestingplayground.com/')

        progress_bar_link = driver.find_element(
            By.XPATH, '//a[contains(text(), "Progress Bar")]'
        )
        progress_bar_link.click()

        logging.info('Progress started')
        progress_start = driver.find_element(
            By.XPATH, '//*[@id="startButton"]'
        )
        progress_start.click()

        progress_bar = driver.find_element(
            By.XPATH, '//*[@id="progressBar"]'
        )
        progress_stop = driver.find_element(
            By.XPATH, '//*[@id="stopButton"]'
        )

        while True:
            show_attr = progress_bar.get_attribute('aria-valuenow')
            if int(show_attr) >= 75:
                progress_stop.click()
                break

        logging.info(f'Progress stopped at: {show_attr}%')
        result = driver.find_element(
            By.XPATH, '//*[@id="result"]'
        )
        result_text = result.text

        duration = extract_duration(result_text)
        logging.info(f'Duration: {duration} ms')

        stopped_value = int(show_attr)
        assert stopped_value == 75, \
            f"Progress did not stop at 75%. Stopped at {stopped_value}%."

    except NoSuchElementException as e:
        logging.error(f'Element not found: {e}')
        raise
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        raise
    finally:
        input("Press any key to continue...")
        driver.quit()


if __name__ == "__main__":
    main()


# Anna correct, assertion of stop value is additional in this case