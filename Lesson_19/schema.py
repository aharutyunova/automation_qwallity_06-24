from marshmallow import Schema, fields


class ExpectedSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
