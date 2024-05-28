
"""
Navigate to "http://www.uitestingplayground.com/"

Go to Text Input, enter any text,
click the button and check if the button text is the same as the entered text.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import os


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


def main():
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get('http://www.uitestingplayground.com/')

        text_input_link = driver.find_element(
            By.XPATH, '//a[contains(text(), "Text Input")]'
        )
        text_input_link.click()

        logging.info('Entering text into input field')
        input_field = driver.find_element(
            By.XPATH, '//*[@id="newButtonName"]'
        )
        input_text = 'Any Text'
        input_field.send_keys(input_text)

        logging.info('Clicking the button')
        btn = driver.find_element(
            By.XPATH, '//*[@id="updatingButton"]'
        )
        btn.click()

        btn_value = btn.text
        logging.info(f'Button text after click: {btn_value}')
        assert btn_value == input_text, \
            f"Button did not change its name to: \
                {input_text}. Actual: {btn_value}"

    except Exception as e:
        logging.error(f'An error occurred: {e}')
        raise
    finally:
        input("Press any key to continue...")
        driver.quit()


if __name__ == "__main__":
    main()
