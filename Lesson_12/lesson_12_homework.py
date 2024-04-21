import logging 
import os

path = os.getcwd()
full_path = os.path.join(path, 'Lesson_12')
os.chdir(full_path)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log_lesson12.log', 
                    filemode='w+', 
                    encoding='utf-8')

"""Create method where you open file,
write there about what is most difficult and what is most easy for you in python.
Put your code in "try except finally" block in case if something will go wrong with
opening/writing file. Handle exception in log file.
"""

def method():
    try:
        with open('python.py', 'w+', encoding = 'utf-8') as f:
            f.writelines(["'The most difficult in python is to not assert it with JS'\n", "'The most easy is syntax'\n"])
    except FileExistsError as fe:
        print(str(fe))
    finally:
        print("File exists in anyway")

method()


# Anna - correct, only would be better log errors not print it - logging.error(fe)