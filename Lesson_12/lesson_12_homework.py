import logging 
import os
# os.chdir("c:/automation_qwallity_06-24/Lesson_12")  # Anna - path is hardcoded

logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log.log', 
                    filemode='a+', 
                    encoding='utf-8')

"""Create method where you open file,
write there about what is most difficult and what is most easy for you in python.
Put your code in "try except finally" block in case if something will go wrong with
opening/writing file. Handle exception in log file.
"""

try:
    with open("AboutPython.txt", "a+", encoding="utf8" ) as f:
        f.write('''The Python's syntax is easy.\
The most difficulty is to remember every lesson for short period.We need to practice a bit more.''')
except IOError as x:
    logging.error(x)
finally:
    print("The 'try except' is finished")


# Anna - correct, what abot lack of time, course really very intensive, mostly python part, in selenium part workshop parts are more
# But in python part I will try find time parallel to our new lessons, for workshops and practical work