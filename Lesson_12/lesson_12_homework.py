"""Create method where you open file,
write there about what is most difficult and what is most
# easy for you in python.
Put your code in "try except finally" block in case if
#something will go wrong with
opening/writing file. Handle exception in log file.
"""

import logging
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='ab_python_error_log.log',
                    filemode='w+',
                    encoding='utf-8')


def python_difficulties_and_ease():
    os.chdir("Lesson_12")
    try:
        with open("python_difficulties_and_ease.txt", "r") as ab_python_file:
            ab_python_file.write("Difficulties:\n\tIndentation\n\tAccess Modifiers\n\tMany types of lists\n\tSelf\n\nEase:\n\tDynamic Typing")
    except Exception as e:
        logging.error(f'An error occurred:{e}')
# if you change "w+" into "r" you can see the error in log file
    finally:
        print("Execution complete")


python_difficulties_and_ease()

# Anna very good !!!