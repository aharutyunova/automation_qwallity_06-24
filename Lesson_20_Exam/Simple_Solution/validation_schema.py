from marshmallow import Schema, fields, ValidationError
import logging


class ApiSchema(Schema):
    user_id = fields.String(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(required=True)

    def check_validation(self, json_data):
        try:
            ApiSchema().load(json_data)
        except ValidationError as x:
            logging.error(x.messages)
        else:
            logging.info("Validation ok")
            return True
