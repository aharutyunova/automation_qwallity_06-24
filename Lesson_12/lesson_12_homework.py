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


def about_python():
    try:
        with open("my_about_python", "w+", encoding="utf8") as file:
            file.writelines("Difficult part for me in python: \n 1. Decision Making Statements_Loops\n 2. OOP\n 3. The reason is that there is a lot of information and little time to study.\n")
            file.writelines("Easy part for me in python: \n 1. Collections.\n 2. I like that you can print your code right away and see the result. \n")   
    except FileNotFoundError:
        logging.error("File not found.")
    except Exception as e:
        logging.error(e)
    finally:
        logging.info("File writing completed successfully.")
        file.close()


about_python()

# Anna - Good implemented, everything is correct
# What about notes about difficulties - Course really intensive, 4 months from one side is long time,
#  but in the same time we have a lot to cover during that time
# From Time to Time I will try to find ways to focus out more on some parts
# But Anyway I am sure as we very often will use loops/if else, not so often but also OOP, so 
# all gaps will be covered with pracice