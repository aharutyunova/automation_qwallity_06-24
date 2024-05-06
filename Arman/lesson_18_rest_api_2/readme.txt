Project Overview
This project includes a set of Python scripts for interacting with a course management API.
 Below is an overview of the key files and their functionalities:

config_file.py: Configuration file where environment variables and credentials for authorization are stored.
api_endpoints.py: Contains all necessary API endpoints used in the project.
login.py: Handles authorization by sending requests to the login API to obtain an access token.
add_course.py: Provides functionality to add a new course to the database.
update_course.py: Updates an existing course in the database based on the course ID.
get_fundamental.py: Retrieves a fundamental course by ID if it exists in the database.
delete_course.py: Deletes a course by ID if it exists in the database.

Usage
Ensure the config_file.py is properly configured with the required credentials and environment variables.
Use the respective Python scripts to perform the desired operations on the course management API.