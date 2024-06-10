from selenium import webdriver

# Ray jan even a lot of part is not complete but it's clear that you're on the right way )))
from Helpers.basic_page import Basic_Helper
from Helpers import logging_config
from Pages.practice import Practice_Page
from Pages.login import Login_Page
import testdata
import config
import logging

def test():
    # 1. Open Chrome browser
    driver = webdriver.Chrome()
    bp = Basic_Helper(driver)
    logging_config.configure_logging()
    practice_page = Practice_Page(driver)
    login_page = Login_Page(driver)

    # 2. Navigate to https://www.letskodeit.com/practice
    bp.geturl(config.url)
    # 3. Click to open the Alert popup
    practice_page.findandclick(practice_page.alert_loc)
    # 4. Get text from the popup and log it
    practice_page.swithtoalert()
    #5. Locate the following element, hide it, check element is hidden
    practice_page.locateAndHideEl()
    #  7. Scroll and click to the Mouse Hover button and Click on Top option to go to the top of screen
    practice_page.goTopOfScreen()
    # 8. Go to the footer and log footer text
    footer = practice_page.scrolluntilelement(practice_page.footer_loc)
    logging.info(footer.text)
    
    # 9. Click on the Sign In button
    practice_page.findandclick(practice_page.signIn_btn)
    
    # # 10. Fill the fields with incorrect email or password and click the LogIn button
    # login_page.incorrectLogin(testdata.email,testdata.password)

    # # 11. Get validation message and log it
    # validation = login_page.locelement(login_page.incorrect_login_text_loc)
    # message = validation.text
    # logging.info(f"Validation message for incorrect login: {message}")


    logging.info("Test is Pass")
    driver.quit()


if __name__ == '__main__':
    test()

