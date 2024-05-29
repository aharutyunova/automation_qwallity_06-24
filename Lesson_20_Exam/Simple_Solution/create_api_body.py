import re


def api_body():
    # Read data from txt file
    with open("input_data.txt") as f:
        data = f.read()
    # Create body json from txt file
    data_without_comment = re.findall(r"^(?!#).+$", data, re.MULTILINE)
    input_data = re.split('\t', data_without_comment[0])
    api_body = {}
    api_body['user_id'] = input_data[0].split(':')[0].strip()
    api_body['title'] = input_data[0].split(':')[1].strip()
    api_body['body'] = input_data[1].strip()
    return api_body
