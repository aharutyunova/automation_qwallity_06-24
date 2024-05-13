import logging

from marshmallow import Schema, fields, ValidationError

from register_user import registered_user_data

log_file_path = r'C:\Users\arman.petrosyan\Desktop\Qwallity\Arman\lesson_20_exam\out.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file_path,
    filemode='w+'
)


# Define the validation schema
class ValidationSchema(Schema):
    userId = fields.Int(required=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)


# Create an instance of ValidationSchema
validation_schema = ValidationSchema()

try:
    # Validate the user_data against the schema
    result = validation_schema.load(registered_user_data['0'])
    print("Validation successfully passed.")
except ValidationError as e:
    print(f"ValidationError: {e.messages}")
    logging.error("Validation failed: %s", e.messages)
