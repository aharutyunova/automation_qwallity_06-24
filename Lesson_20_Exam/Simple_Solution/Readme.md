# Data Posting and Validation Program

This Python program reads data from a given input_data.txt file, posts the data to a specified REST endpoint (see below), 
and performs validation on the returned data. The program then compares the returned data with the sent data,
ensuring that UserID, Title, Body fields are present and have the same values.
The status of each operation is recorded in a log file.


The program will perform the following actions:

- Read data from the input file.
- Post the data to the specified REST endpoint.
- Validate the returned data.
- Compare the returned data with the sent data.
- Record data send result in log file

endpoint -> https://jsonplaceholder.typicode.com/posts

# Prerequisites

Before running the program, ensure that you have the following:
Used library:                       - requests
                                    - logging
                                    - re
                                    - json
                                    - marshmallow
                                    - validation

main.py                             - the python file contains the logic of task
create_api_body.py:                 - get data from input_data.txt and create body dictionary
validation_schema.py                - validate given json structure     
send_api.py                         - send post requests, validate data and if validation pass, return result
config.json:                        - the file with api endpoint, log file name and path
input_data.txt                      - the input data text file 

# Usage
Open folder, so Simple_Solution be the root folder,  the Run main.py file
