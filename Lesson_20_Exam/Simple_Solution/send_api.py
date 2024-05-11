import validation_schema
import requests


def get_api_response(api_endpoint, json_data):
    result = requests.post(api_endpoint, json=json_data).json()
    schema_obj = validation_schema.ApiSchema()
    validate = schema_obj.check_validation(result)
    if validate:
        return result
