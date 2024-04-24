from marshmallow import Schema, validate, fields, ValidationError
import json
import os
from converterFile import converter

class ExpectedSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    address = fields.String(required=True, validate=validate.OneOf(['Yerevan','Gyumri','Vanadzor']))


my_data = converter('my_data.json','Lesson_15')
try:
    result = ExpectedSchema().load(my_data)

except ValidationError as err:
    print(err.messages)
else:
    print('name:', result['name'])
    print('surname:', result['surname'])
    print('address:', result['address'])


# Anna - Good, you covered  flow per requirements