import json


def load_config(config_file_path):
    with open(config_file_path, 'r') as f:
        config_data = json.load(f)
    return config_data
