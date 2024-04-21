def Validate_data(data):

    if validate_result(data, dict):
        print("Validation is successful!")
    else:
        print("Validation is failed: Data is not in the expected format.")
        
