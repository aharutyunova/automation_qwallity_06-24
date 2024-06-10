from selenium import webdriver
from Pages.firstLogin import First_Login
from Pages.secondLogin import Second_Login
from Pages.balance import Balance
import config
import testdata
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='loggingInfo.log', 
                    filemode='w+', 
                    encoding='utf-8')

def test():
    try:
        driver = webdriver.Chrome()
        fl = First_Login(driver)
        sl = Second_Login(driver)
        b = Balance(driver)
        
        fl.geturl(config.base_url)
        fl.firstLogin(testdata.email, testdata.code)
        fl.findandclick(fl.navigation_bar_login)
    except Exception as err:
        logging.error(f"First login failed, there is an error {err}")   
    try:
        sl.secondLogin(testdata.username, testdata.password)
    except Exception as err:
        logging.error(f"Second login failed, there is an error {err}")   

    try:
        b.findandclick(b.user_action_button)
        initial_balance = b.getElementValue(b.accbalance_loc)
        b.addBalance(testdata.amount)
        changed_balance = b.getElementValue(b.accbalance_loc)
        assert (float(initial_balance) + float(testdata.amount))==float(changed_balance), logging.info(f"{changed_balance} not equal to {initial_balance} + {testdata.amount}")
        logging.info(f"Changed balance {changed_balance} equal initial balance {initial_balance} + amount {testdata.amount}")
    except Exception as err:
        logging.error("An unexpected error occurred on balance page")
    finally:
        driver.quit()
test()