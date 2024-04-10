
"""Create method where you open file,
write there about what is most difficult and what is most easy for you in python.
Put your code in "try except finally" block in case if something will go wrong with
opening/writing file. Handle exception in log file.
"""

import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log.log', 
                    filemode='a+', 
                    encoding='utf-8')

import os
current = os.getcwd()
os.chdir(r"C:\Users\Public\automation_qwallity_06-24\Lesson_12_Armine")

try:
    with open("Strengths and Weaknesses.txt", mode='w+', encoding ="utf8") as file:
        print(filewrite("My weaknesses\n 1.working with dictionaries\n 2.loops\n 3.syntax and tabulations\n")) #I wrote with mistake, so that see error in the logs))
        print(file.write("My strengths\n 1.Working with Classes\n 2.if/elses\n 3.OOP in general\n"))
except Exception as e:
    logging.error(e)
finally:
    print("File should have been created")

#Please also show me how to see logs for each steps, I tried but I could not. 
#Anna jan, would you please also check Lesson_11))

#And I want to say that you are the best teacher, cause you do your best to explain such a complicated course in the simplest way. 
#Before I thought it is something I could not understand, but thanks to you, now I like and understand almost everything and can write my own code somehow.
#I hope, that the rest of the course will go on in this way, and we will finish course successfully)) Thank you very much!

