Configuration File: The logging configuration is stored in a JSON format in the config.json file.

Logging File Name: The logging file name is specified in the config.json file under the key "log_file_name".
If not specified, it defaults to out.log.

API Endpoint: The registered API endpoint is specified in the config.json file.

User registration data: User data store in dictionary in the data.json file already filtered by regular expression

The application can be executed by running main.py. This file contains the main entry point for the
application and executes the full application flow.

Register user .py file has a function that will register user data

This application filters commented string data stored in a text.txt file using regular expressions.

Read File: Read the content of the text.txt file.
Filter Commented Lines: Use regular expressions to filter lines starting with # in the txt_to_json_converter.py.
Display Filtered Data: Display the filtered lines.

Validation can be checked in the validate_user_data.py file where checking all required keys of dictionary