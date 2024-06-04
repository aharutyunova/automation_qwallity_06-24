def run_driver(input_driver, url):
    """Function run web browser driver with given URL"""
    driver = input_driver.Chrome()
    driver.get(url)


def close_browser(input_driver):
    """Function close tabs and browser"""
    input_driver.quit()


def wait(input_driver):
    """Function stops application with fixed seconds"""
    input_driver.implicitly_wait(10)


def check_hidden(input_style):
    """Function checks input field hidden"""
    hidden_style = "display: none;"
    if hidden_style in input_style:
        return "Hide/Show input field hidden"
    else:
        return "Hide/Show input field show"
