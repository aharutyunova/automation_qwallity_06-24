from marshmallow import Schema, fields, ValidationError

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


class Jsonvalidation (Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True)
    phone = fields.Int(required=True)

def text_validation_funct(js_file):
    try:
        Jsonvalidation().load(js_file)
    except ValidationError as val:
        logging.error(val.messages)
    else:
        logging.info("Validation is passed successfully")
    
        return True
        



    