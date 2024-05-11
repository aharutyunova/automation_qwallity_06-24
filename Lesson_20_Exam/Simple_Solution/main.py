import json
import logging
import send_api
import create_api_body

# Get data from config.json
with open('config.json', 'r+') as f:
    data = f.read()
    config_data = json.loads(data)

logging.basicConfig(filename=config_data['log_file_name'],
                    encoding='utf-8',
                    format='%(levelname)s - %(message)s',
                    level=logging.INFO,
                    filemode='w+')
# Send data with post request

api_body = create_api_body.api_body()
api_response = send_api.get_api_response(config_data['api_url'],
                                         json_data=api_body)

# If response exists and validation is passed remove
#  'id' key before data comparison

if api_response:
    api_response.pop('id')
    logging.info("Response json validation schema passed")
else:
    logging.info("Response json validation schema failed")


assert api_response == api_body,  logging.error(
    f"Incorrect response!{api_response}")
logging.info("Response body is equal to Request body")
