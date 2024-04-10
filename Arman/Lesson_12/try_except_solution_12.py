import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='log.log',
    filemode='w+',
    encoding='utf-8'
)

"""Create method where you open file,
write there about what is most difficult and what is most easy for you in python.
Put your code in "try except finally" block in case if something will go wrong with
opening/writing file. Handle exception in log file.
"""


def my_python_skills():
    current_file_path = os.path.join(os.getcwd(), "my_python_skills.txt")
    try:
        with open(current_file_path, 'w') as file:
            file.writelines("Easy: Everything is clear and easy what we have "
                            "learned until 12 lesson \n")
            file.writelines("Difficult: There is no difficult part of Python yet for me \n")
        logging.info("Info was successfully logged")
    except Exception as er:
        logging.error(er)


my_python_skills()
