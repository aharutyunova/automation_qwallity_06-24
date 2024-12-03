from marshmallow import Schema, validate, fields, ValidationError

class Advanced_Course_Schema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)

def validate_advanced_courses(courses):
    for course in courses:
        try:
            Advanced_Course_Schema().load(course)
        except ValidationError as err:
            print(err.messages)
            return False
    print("Validation has passed successfully")
    return True
