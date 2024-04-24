import re
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


try:
    new_dict = {}
    with open("config.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            match = re.match(r'\s*([^#][\w\s]+)\s*=\s*([^#]+)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                new_dict[key] = value
    print("New dictionary will be:", new_dict)

except Exception as e:
    logging.error(f"Error occurred: {e}")
