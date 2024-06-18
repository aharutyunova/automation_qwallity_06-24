# Random Course Data Validator and Writer

## Overview
This Python program retrieves random course data from an API, validates it against a predefined schema, and writes the validated data to a JSON file.

## Features
- Retrieves random course data from an API endpoint.
- Validates the retrieved data against a predefined schema.
- Writes the validated data to a JSON file for further analysis or processing.

## Usage
1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the `main.py` script using `python main.py`.
3. The program will retrieve random course data, validate it, and write the validated data to a file named `valid_data.json`.

## Dependencies
- Python 3.x
- `requests` library for making HTTP requests
- `marshmallow` library for schema validation

## Configuration
- Instead of using Environment vaiables just remove "#" from the 3rd line and comment the 8th and 9th lines of the login.py file
- If you want to use Environment vaiables you shoud add the appropeiate key: values of the username and password in your System Environment vaiables 
    username = "qwallity_admin_user", "default_value"
    password = "qwallity_password", "default_value"
- After setting the environment variables, make sure to restart your shell or IDE to ensure that the changes take effect. 
- Create Virtual Environment: Navigate to the project directory and by using `python -m venv env` command in terminal create a virtual environment.

# The part about the .bat file is incomplete․ I have an issue that I haven't looked into yet. So, I'll finish it later on in the future