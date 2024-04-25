import logging
import re
import json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def parse_config_file(file_path='config_data.txt'):
    config_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                match = re.match(r'^\s*([^=]+)\s*=\s*([^#]+)(?:#.*)?$', line)
                if match:
                    key = match.group(1).strip()
                    value = match.group(2).strip()
                    config_data[key] = value
                else:
                    logging.warning(f"Ignoring line due to invalid format: {line}")
    except FileNotFoundError:
        logging.error(f"Config file '{file_path}' not found.")
    except Exception as e:
        logging.error(f"An error occurred while parsing config file: {e}")
    return config_data



parsed_data = parse_config_file()
parsed_data_str = json.dumps(parsed_data, indent=4)
print(parsed_data_str)
