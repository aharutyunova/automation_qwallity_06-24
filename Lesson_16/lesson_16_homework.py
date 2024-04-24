import os
import json
import logging
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def parse_config(file_path):
    try:
        with open(file_path, "r") as file:
            res_dict = {}
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue
                match = re.match(r'\s*([\w\s]+)\s*=\s*([\w\s]+)', line)
                if match:
                    key = match.group(1).strip()
                    value = match.group(2).strip()
                    res_dict[key] = int(value)
            return res_dict
    except Exception as e:
        logging.error(f"Error found: {e}")
    finally:
        logging.info("File parsing completed")


current_directory = os.getcwd()
file_name = 'config_file.txt'
full_file_path = os.path.join(current_directory, file_name)
new_res_dict = parse_config(full_file_path)
print("Resulting dictionary:", new_res_dict)
print(json.dumps(new_res_dict, indent=4))
