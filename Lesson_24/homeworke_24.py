from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def test_visibility(driver):
    try:
        vis_btn = driver.find_element(By.XPATH, "//a[@href='/visibility']")
        actions = ActionChains(driver)
        actions.move_to_element(vis_btn).click().perform()
        logging.info("Opened Visibility page")

        hide_button = driver.find_element(By.XPATH, "//button[@id='hideButton']")
        hide_button.click()
        logging.info("Clicked Hide button")

        buttons_xpath = [
            "//tbody/tr[1]/td[2]",
            "//button[@class='btn btn-warning zerowidth']",
            "//div[@id='hidingLayer']",
            "//button[@style='opacity: 0;']",
            "//button[@style='visibility: hidden;']",
            "//button[@style='display: none;']",
            "//button[@class='btn btn-info offscreen']"
        ]

        all_hidden = False
        for xpath in buttons_xpath:
            try:
                button = driver.find_element(By.XPATH, xpath)
                if button.is_enabled():
                    all_hidden = True
                    continue
                else:
                    logging.info("Not all buttons are hidden")
                    all_hidden = False
                    break
            except Exception as e:
                logging.error(f"Exception occurred while checking button visibility: {e}")
                all_hidden = False

        if all_hidden:
            logging.info("All buttons are hidden as expected")
            logging.info("Visibility test passed")
        else:
            driver.save_screenshot("scrn.png")
            logging.warning("Not all buttons are hidden")
    except Exception as e:
        logging.error(f"Visibility Test failed: {e}")


def test_progress_bar(driver):
    try:
        driver.find_element(By.XPATH, "//a[@href='/progressbar']").click()
        logging.info("Opened Progress Bar page")

        start_button = driver.find_element(By.XPATH, "//button[@id='startButton']")
        start_button.click()
        logging.info("Clicked Start button")

        time.sleep(2)

        stop_button = driver.find_element(By.XPATH, "//button[@id='stopButton']")
        stop_button.click()
        logging.info("Clicked Stop button")

        duration = driver.find_element(By.XPATH, "//div[@id='progressBar']").text
        logging.info(f"Duration is {duration}")
        logging.info("Progress Bar test passed")

    except Exception as e:
        logging.error(f"Progress Bar Test failed: {e}")


def test_text_input(driver):
    try:
        driver.find_element(By.XPATH, "//a[@href='/textinput']").click()
        logging.info("Opened Text Input page")

        text_input = driver.find_element(By.XPATH, "//input[@id='newButtonName']")
        text_button = driver.find_element(By.XPATH, "//button[@id='updatingButton']")
        test_text = "QWALLITY"
        text_input.send_keys(test_text)
        text_button.click()
        time.sleep(2)
        logging.info("Entered text and clicked button")

        button_text = text_button.text
        if button_text == test_text:
            logging.info("Text Input Test: Button text matches the entered text.")
            logging.info("Text Input test passed")
        else:
            logging.warning(
                f"Text Input Test: Button text '{button_text}' does not match the entered text '{test_text}'.")

    except Exception as e:
        logging.error(f"Text Input Test failed: {e}")


if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()
        driver.get("http://www.uitestingplayground.com")
        driver.maximize_window()
        time.sleep(2)

        test_visibility(driver)
        driver.back()
        time.sleep(2)

        test_progress_bar(driver)
        driver.back()
        time.sleep(2)

        test_text_input(driver)
    finally:
        driver.quit()