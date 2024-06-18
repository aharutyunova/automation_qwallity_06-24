import re
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


class Data_Parser:
    def parse_text_to_dict(data_file, regex_pattern):
        try:
            with open(data_file, "r") as f:
                text = f.read()
                replaced_text = re.findall(regex_pattern, text)
                res = {key: int(value) for key, value in replaced_text}

                formatted_res = "{\n"
                for key, value in res.items():
                    formatted_res += f'    "{key}": {value},\n'
                formatted_res += "}"

                logging.info("Successfully parsed the file and created the dictionary.")
                return formatted_res
        except Exception as e:
            logging.error(f"An error occurred: {e}")
