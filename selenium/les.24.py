from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log_file.log',
                    filemode='w+',
                    encoding='utf8')

WAIT_TIME = 30

browsers = ["Chrome", "Firefox"]

for browser in browsers:
    try:
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Firefox":
            driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get("https://www.letskodeit.com/practice")
        time.sleep(5)

        wait = WebDriverWait(driver, 10)

        btn_alert = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="alertbtn"]')))
        btn_alert.click()
        time.sleep(2)

        alert = driver.switch_to.alert
        alert_text = alert.text
        expected_text = "Hello , share this practice page and share your knowledge"
        alert.accept()
        time.sleep(2)

        def visibility_test():
            show_button = driver.find_element(By.XPATH, '//*[@id="show-textbox"]')
            hide_button = driver.find_element(By.XPATH, '//*[@id="hide-textbox"]')
            displayed_text_box = driver.find_element(By.XPATH, '//*[@id="displayed-text"]')

            show_button.click()
            time.sleep(2)
            assert displayed_text_box.is_displayed(), "Text box should be visible after clicking 'Show' button"
            print("Hide/Show Example is visible")

            hide_button.click()
            time.sleep(2)
            assert not displayed_text_box.is_displayed(), "Text box should not be visible after clicking 'Hide' button"
            print("Hide/Show Example not displayed")

        visibility_test()

        mouse_hover_button = driver.find_element(By.ID, "mousehover")
        driver.execute_script(
            "arguments[0].scrollIntoView();", mouse_hover_button
            )

        actions = ActionChains(driver)
        actions.move_to_element(mouse_hover_button).perform()

        top_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mouse-hover-example-div"]//a[text()="Top"]')))
        top_option.click()
        time.sleep(5)  
    
        footer = driver.find_element(By.XPATH, '//*[@id="page"]/div[3]/div/div/div[1]/div/div[1]/p')
        expected_footer_text = "© 2024 letskodeit"
        assert footer.text.strip() == expected_footer_text, f"Expected footer text: {expected_footer_text}, but got: {footer.text.strip()}"

        # Click the sign-in button
        sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a')))
        sign_in_btn.click()
        time.sleep(5) 

        username = driver.find_element(By.XPATH, "//*[@id='email']")
        username.send_keys("you@gmail.com")
        password = driver.find_element(By.XPATH, "//*[@id='login-password']")
        password.send_keys("your_password")
        submit = driver.find_element(By.XPATH, "//*[@id='login']")
        submit.click()
        time.sleep(5)
        conf_message = driver.find_element(By.XPATH, '//*[@id="incorrectdetails"]')
        assert conf_message(), "Incorrect login details. Please try again."
        time.sleep(5)

        # Open a new tab and switch to it
        
        driver.execute_script("window.open('about:blank', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)

        driver.get("https://www.python.org/")
        time.sleep(10) 

        search = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
        search.clear()
        search.send_keys("Automation")
        search.send_keys(Keys.RETURN)

        wait = WebDriverWait(driver, 10)
        results = wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, '.list-recent-events li'))
            )

        num_results = len(results)
        logging.info(f'Number of results found on the first page: {num_results}')

        print(f'Number of results found on the first page: {num_results}')

    except Exception:
        logging.exception("An exception occurred")
    finally:
        driver.quit()
