import json
import jsonschema
import os


courses_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"}
        },
        "required": ["id", "title"]
    }
}


def write_json(data):
    try:
        jsonschema.validate(instance=data, schema=courses_schema)
        print("Courses data is valid!")
        current_directory = os.getcwd()
        json_file = r'courses_data.json'
        file_path = os.path.join(current_directory, json_file)
        if file_path:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4) 
                print("Courses data has been written to courses_data.json")
    except jsonschema.ValidationError as e:
        print("Validation Error:", e)
