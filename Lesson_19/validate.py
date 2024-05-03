from marshmallow import Schema, fields, ValidationError


class CourseSchema(Schema):
    id = fields.Int(required=True)
    title = fields.String(required=True)


def validate(data: list) -> bool:
    try:
        schema = CourseSchema(many=True)
        schema.load(data)
        return True
    except ValidationError:
        return False