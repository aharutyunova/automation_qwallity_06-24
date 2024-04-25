import logging
import re

from text import test_text

text = test_text

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w+',
    encoding='utf-8'
)

"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed 55 55 55 55 consequat nisl sed quam consequat, ac +37495656565 venenatis 95-12-12-21 justo vehicula.
Nulla facilisi. Maecenas a nisi eget justo congue suscipit.
Integer euismod 095121515 mauris id dui malesuada, nec lobortis risus consequat.
"""

# |\b\d{9,11}\b
def find_all_phone_numbers(input_file):
    if input_file:
        try:
            phone_pattern = r"\+?\d{2,3}[-\s]?\d{2,3}[-\s]?\d{2,3}[-\s]?\d{2,3}"
            phone_numbers = re.findall(phone_pattern, text)
            return phone_numbers
        except Exception as error:
            logging.error(error)
    else:
        logging.error("File is not exist")


get_numbers = find_all_phone_numbers(text)

for number in get_numbers:
    print(number)
