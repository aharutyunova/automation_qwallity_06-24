This program sends data from a text file to a REST endpoint, validates the returned data,
and logs the status to a specified log file.

Usage:
python main.py <config_file_path>, <data_file_path>

Requirements:
- Python 3.x
- requests library (install using 'pip install requests')
- Ensure config file follows JSON format as specified in config.json
- Ensure data file follows the specified format as demonstrated in data.txt
