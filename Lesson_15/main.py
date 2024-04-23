from json_convertor import Json_Convertor
from schema_valid import ExpectedSchema
from marshmallow.exceptions import ValidationError


json_conv = Json_Convertor()

json_data = json_conv.json_load("contacts.json")

try:
    ExpectedSchema().load(json_data)
except ValidationError as e:
    print(e.messages)
else:
    print("Validation passed")


json_conv.json_dump(json_data, "new_contacts.json")


# Anna jan I have some mistake but I can't find where and what ((( And it stops me
# Please heeeelp ))
