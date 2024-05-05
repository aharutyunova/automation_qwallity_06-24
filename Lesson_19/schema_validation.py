from marshmallow import Schema, validate, fields, ValidationError

class AdvCourseSchema(Schema):
    id = fields.Number(required=True)
    title = fields.String(required=True)

def validate_adv_courses(courses):
    for course in courses:
        try:
            AdvCourseSchema().load(course)
            continue
        except ValidationError as ValERR:
            print(ValERR.messages)
            break
            return False
    print("Validation has passed")
    return True