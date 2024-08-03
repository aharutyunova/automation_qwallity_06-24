
"""Create method where you open file,
write there about what is most difficult and what is most easy for you in python.
Put your code in "try except finally" block in case if something will go wrong with
opening/writing file. Handle exception in log file.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def write_method():
    try:
        with open("new_file.txt", 'w') as f:
            f.write("The most difficult aspect for me is understanding Object-Oriented Programming (OOP) in Python.\n")
            f.write("Python variables, loops, conditional operator were very easy for me.\n")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    finally:
        pass


write_method()

# Anna - well done
# What about OOP, I am sure you will cover all gaps with time, and it is not be so difficult for you,
# as you understand coding very well