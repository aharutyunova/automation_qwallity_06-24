import os
from config_parser import Data_Parser


current_dir = os.path.dirname(os.path.abspath(__file__))

data_file = os.path.join(current_dir, "config_data.py")

regex_pattern = r'(\w+)\s*=\s*(\d+)'
replaced_text = Data_Parser.parse_text_to_dict(data_file, regex_pattern)
print(replaced_text)
print(type(replaced_text))


# Anna - very good solution and optimal regex pattern