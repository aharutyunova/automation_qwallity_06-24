from marshmallow import Schema, fields


class SchemaValidation(Schema):
    userId = fields.Int(required=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)
    id = fields.Int(required=False)


def validate_response(sent_data, response_data):
    if sent_data['userId'] != response_data['userId']:
        return False
    if sent_data['title'] != response_data['title']:
        return False
    if sent_data['body'] != response_data['body']:
        return False
    return True
