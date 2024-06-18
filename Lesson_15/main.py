import os
from json_convertor import Json_Convertor
from schema_valid import ExpectedSchema
from marshmallow.exceptions import ValidationError

current_dir = os.path.dirname(os.path.abspath(__file__))

contacts_file_path = os.path.join(current_dir, "contacts.json")
new_contacts_file_path = os.path.join(current_dir, "new_contacts.json")

json_conv = Json_Convertor()

json_data = json_conv.json_load(contacts_file_path)

try:
    ExpectedSchema().load(json_data[0])
except ValidationError as e:
    print(e.messages)
else:
    print("Validation passed")

json_conv.json_dump(new_contacts_file_path)


# Anna jan I have some mistake but I can't find where and what ((( And it stops me
# Please heeeelp ))

# Anna - Lusine jan you got error, because you give as argument not json type but list type - in line 16 I added [0] index, everything works now :)