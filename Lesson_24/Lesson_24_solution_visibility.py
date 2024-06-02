"""
Navigate to "http://www.uitestingplayground.com/"

Go to Visibility, click the Hide button.
Check in your program that buttons are hidden.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

        visibility = driver.find_element(By.XPATH, '//a[@href="/visibility"]')
        visibility.click()

        hide_btn = driver.find_element(By.XPATH, '//*[@id="hideButton"]')
        hide_btn.click()

        try:
            removed_btn = driver.find_element(
                By.XPATH, '//*[@id="removedButton"]'
            )
            assert not removed_btn.is_displayed(), \
                "Failed - removed button should be hidden"
        except NoSuchElementException:
            logging.info(
                'Pass - removed button does not exist in the DOM or hidden'
            )
        except AssertionError as e:
            logging.error(e)

        try:
            zero_width_btn = driver.find_element(
                By.XPATH, '//*[@id="zeroWidthButton"]'
            )
            width = driver.execute_script(
                "return arguments[0].offsetWidth;", zero_width_btn
            )
            assert width == 0, "Failed - Zero width button should be hidden"
            logging.info(
                f'Pass - zero width button is hidden (width is {width})'
            )
        except NoSuchElementException:
            logging.error('zero width button does not exist in the DOM')
        except AssertionError as e:
            logging.error(e)

        try:
            hidingLayer = driver.find_element(
                By.XPATH, '//*[@id="hidingLayer"]'
            )
            height = driver.execute_script(
                "return arguments[0].offsetHeight;", hidingLayer
            )
            assert height != 0, "Failed - overlapped button should be hidden"
            logging.info(
                f'Pass - overlapped button is hidden \
                    (hidden layer height: {height})'
            )
        except NoSuchElementException:
            logging.error('overlapped button does not exist in the DOM')
        except AssertionError as e:
            logging.error(e)

        try:
            transparent_btn = driver.find_element(
                By.XPATH, '//*[@id="transparentButton"]'
            )
            show_attr = transparent_btn.get_attribute('style')
            assert show_attr, "Failed - transparent button should be hidden"
            logging.info('Pass - transparent button is hidden')
        except NoSuchElementException:
            logging.error('transparent button does not exist in the DOM')
        except AssertionError as e:
            logging.error(e)

        try:
            invisible_btn = driver.find_element(
                By.XPATH, '//*[@id="invisibleButton"]'
            )
            show_attr = invisible_btn.get_attribute('style')
            assert show_attr, "Failed - invisible button should be hidden"
            logging.info('Pass - invisible button is hidden')
        except NoSuchElementException:
            logging.error('invisible button does not exist in the DOM')
        except AssertionError as e:
            logging.error(e)

        try:
            notdisplayed_btn = driver.find_element(
                By.XPATH, '//*[@id="notdisplayedButton"]'
            )
            show_attr = notdisplayed_btn.get_attribute('style')
            assert show_attr, "Failed - notdisplayed button should be hidden"
            logging.info('Pass - notdisplayed button is hidden')
        except NoSuchElementException:
            logging.error('notdisplayed button does not exist in the DOM')
        except AssertionError as e:
            logging.error(e)

        try:
            offscreen_btn = driver.find_element(
                By.XPATH, '//*[@id="offscreenButton"]'
            )
            show_attr = offscreen_btn.get_attribute('class')
            assert 'btn btn-info offscreen' in show_attr, \
                "Failed - offscreen button should be hidden"
            logging.info('Pass - offscreen button is hidden')
        except NoSuchElementException:
            logging.error('offscreen button does not exist in the DOM')
        except AssertionError as e:
            logging.error(e)

    except Exception as e:
        logging.error(f'An error occurred: {e}')
        raise
    finally:
        input("Press any key to continue...")
        driver.quit()


if __name__ == "__main__":
    main()

# Anna - Correct :)