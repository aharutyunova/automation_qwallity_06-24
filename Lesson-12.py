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
                    filename='my_log.log', 
                    filemode='w+', 
                    encoding='utf-8')

def write_to_file():
    os.chdir("Lesson_12_Mariam")
    try:
        file_path = "python_difficulties_and_ease.txt"
        with open(file_path, "w") as file:
            print(file.write("Most difficult: Understanding complex list algoritms.\n"))
            print(file.write("Most easy: Working with dictionaries and sets.\n"))
    except Exception as e:
        logging.error(e)
    finally:       
        print("Task completed")