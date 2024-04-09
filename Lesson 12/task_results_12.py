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

class writeafile:
    def write_texts(self):
        try:
            with open("texts.txt", "w+") as file:
                file.write("What's most difficult for me in Python:\n")
                file.write("OOP section is most difficult part in Python.\n")
                file.write("What's most easy for me in Python:\n")
                file.write("Readability and understandability of code errors.\n")
        except Exception as e:
            logging.exception(f"An error occurred: {e}")
        finally:
            print("File writing process completed.")

writer = writeafile()
writer.write_texts()
