import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log.log', 
                    filemode='w+', 
                    encoding='utf-8')

"""Create method where you open file,
write there about what is most difficult and what is most easy for you in python.
Put your code in "try except finally" block in case if something will go wrong with
opening/writing file. Handle exception in log file.
"""

file = "my_log.log"
my_python_skills = input("Please write about your Python skills: ")
try:
    if file:
        with open(file, 'w+') as f:
            f.write(my_python_skills)

# comment line 15 and exception errors will occur

except FileNotFoundError as fn:
    print(f"File not found: {fn}")

except NameError as nm:
    print(f"Variable not found: {nm}")

finally:
    print("Code worked")


# Anna - code structure is correct, only in exception use logging.error() instead of print error message