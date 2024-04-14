import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log_file.log', 
                    filemode='w+', 
                    encoding='utf8')

a = 10
b = "b"
try:
    result = a + b 

except BaseException as be:
    logging.error(be)

else:
    print("true") # only if try is pass

finally:
    print("result") # always is called



price_list = [ 1, 2 , 100 , 200 , -50 ]

try:
    for i in price_list:
        if price_list[i] < 0:
            raise Exception (" Invalid or negative value ")
except:
    logging.error(Exception)


"""Create method where you open file,
write there about what is most difficult and what is most easy for you in python.
Put your code in "try except finally" block in case if something will go wrong with
opening/writing file. Handle exception in log file.
"""