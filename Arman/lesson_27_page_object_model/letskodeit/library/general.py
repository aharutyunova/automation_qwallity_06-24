import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w+',
    encoding='utf-8'
)


def run_driver(input_driver, url):
    """Function run web browser driver with given URL"""
    try:
        input_driver.get(url)
        logging.info(f"Web driver successfully ran and opened {url} page")
    except TimeoutError as error:
        logging.error(error)


def close_browser(input_driver):
    """Function close tabs and browser"""
    input_driver.quit()
    logging.info("Browser closed")


def click_alert_popup(driver, alert_xpath):
    try:
        # Attempt to find the element with id 'alert_button' and click it
        alert_xpath.click()
        # Attempt to switch to the alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        # Accept the alert (click OK)
        alert.accept()
        print("Alert accepted!")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def wait(input_driver):
    """Function stops application with fixed seconds"""
    input_driver.implicitly_wait(10)


def check_hidden(input_style):
    """Function checks input field hidden"""
    hidden_style = "display: none;"
    if hidden_style in input_style:
        return "Hide/Show input field hidden"
    else:
        return "Hide/Show input field is showing"
