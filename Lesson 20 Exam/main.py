import logging
import requests
from config_handler import load_config
from data_parser import parse_data
from request_handler import send_request
from validator import SchemaValidation, validate_response

logging.basicConfig(filename='out.log', level=logging.INFO, format='%(levelname)s - %(message)s')


def main(config_file_path, data_file_path):
    config = load_config(config_file_path)
    endpoint = config.get('endpoint')

    data = parse_data(data_file_path)

    for record in data:
        response = send_request(endpoint, record)
        if isinstance(response, requests.Response):
            if 200 <= response.status_code < 300:
                logging.info(f"Connected to {endpoint}")
                response_data = response.json()
                schema = SchemaValidation()
                try:
                    schema.load(response_data)
                except Exception as e:
                    logging.error(f"Validation error: {e}")
                else:
                    logging.info("Data validated successfully")
                    if not validate_response(record, response_data):
                        logging.error("Data mismatch error")
            else:
                logging.error(f"Error: {response.status_code}")


if __name__ == "__main__":
    main("config.json", "data.txt")
