from marshmallow import Schema, fields, ValidationError
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


class ExpectedSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)


def validate_json_data(json_str):
    try:
        ExpectedSchema().load(json_str)
    except ValidationError as x:
        logging.error(x.messages)
    else:
        logging.info("Json data Validation is passed")
        return True
