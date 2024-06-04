# from Arman.lesson_27_page_object_model.letskodeit.helpers.action import action
from Arman.lesson_27_page_object_model.letskodeit.helpers.driver import driver
# from Arman.lesson_27_page_object_model.letskodeit.helpers.locators import *
# from Arman.lesson_27_page_object_model.letskodeit.helpers.logging import logging
from Arman.lesson_27_page_object_model.letskodeit.helpers.test_data import *
from Arman.lesson_27_page_object_model.letskodeit.library.general import *


# from Arman.lesson_27_page_object_model.letskodeit.pages.practice_page_locators import *
# from Arman.lesson_27_page_object_model.letskodeit.pages.python_page import *

def run_test():
    run_driver(driver, practice_page_url)


if __name__ == '__main__':
    run_test()
