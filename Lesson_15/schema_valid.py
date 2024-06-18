from marshmallow import Schema, fields


class ExpectedSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    is_student = fields.Boolean(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    address = fields.Dict(required=True, keys=fields.String(), values=fields.String())
