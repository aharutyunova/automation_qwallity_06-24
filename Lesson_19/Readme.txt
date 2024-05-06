# General overview

Get Advanced Courses

The "Get Advanced Courses" program is a Python script designed to retrieve information about ten advanced courses, 
including their IDs and titles. It incorporates schema validation to ensure the integrity of the returned data. 
Upon successful validation, the program writes the data to a JSON file.

# Program Strucoture

- login.py: Allows users to authenticate and receive a token to access the system.
- get_adv_course.py: Retrieves ten advanced courses available in the system.
- config_file.py: Stores environment and authorization credentials.
- endpoints_file.py: Contains all the required API endpoints used in the project.
- validate.py: Provides validation schema for checking returned data.
- write_json.py: Contains the logic to write validated JSON data.

# Prerequisites

Before running the program, ensure that you have the following:
Used library:                       - requests (pip install requests)
                                    - marshmallow (pip install marshmallow)
                                    - random



# Usage

To start the program run main_with_logging.py file