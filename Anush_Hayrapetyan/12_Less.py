import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m  %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',)

try:
    with open("Anush_log.log", 'w') as f:
        f.write("Hi Python, you are easy, but I have many difficulties, for example ` 1.OOP, 2.With, Open file. Easy points are 1. Operators, 2.Dictionaries, Arrays, Functions ")

except Exception as te:
    logging.error(f"Error occurred: {te}")

finally:       
    print("Done")
    

# I will send the additional OOP task tomorrow.   

# Anna - Even File path is difficult for you, this task well done :)
# Only will be better to write abiut python in separate file not in the log file