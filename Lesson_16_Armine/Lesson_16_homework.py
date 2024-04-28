'''Create a simple config file parser.
Config file has the following syntax:
Comments begin with # (may be in the beginning of the line or in the middle of the line.
Blank lines are allowed.
Format of string is key = value
Spaces are allowed around assignment. 

Expected output: The data must be loaded into dictionary.
NOTE: Use logging in solution
'''
import logging
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


text = "#This is a comment Width = 4 # box width Height = 3 Length = 6"
patt = (r'\w+\s\=\s\d+')
result = re.findall(patt, text)
print(result)

my_dict = {}
for i in text.split('\n'):
    if "=" in i:
        key, value = i.split("=")
        my_dict[key.strip()] = value.strip()
        print(my_dict)