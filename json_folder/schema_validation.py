

def validate_schema(data):
    required_fields = {"name", "lastname", "address"}
    for field in required_fields:
        if field not in data:
            return False
    return True