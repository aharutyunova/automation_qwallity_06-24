1. prod_env.py: This file defines the production and test environments using dictionaries.
2. data.env: Contains user credentials and API keys necessary for authentication.
3. endpoints.py: Imports environment
4. login.py: Performs authentication using provided credentials 
5. parsing.py: Retrieves data for advanced courses from the FUNDAMENTAL_COURSE_ENDPOINT, validates the response data against a predefined schema, and extracts 10 unique course IDs and titles. The extracted data is then stored in a JSON file named "10_course.json".
6. run_script.bat: A batch file that automates the execution.