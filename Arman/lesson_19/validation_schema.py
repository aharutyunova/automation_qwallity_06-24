from marshmallow import Schema, fields


class ValidationSchema(Schema):
    id = fields.Str(required=True)
    title = fields.Str(required=True)
