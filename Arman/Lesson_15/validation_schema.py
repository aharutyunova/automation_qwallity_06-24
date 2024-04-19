from marshmallow import Schema, fields


class ValidationSchema(Schema):
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    age = fields.Int(required=True)


class MyDataValidation(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    address = fields.Str(required=True)
