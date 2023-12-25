import json


def get_data(path):
    with open(path, encoding='utf-8') as f:
        data_dict = json.load(f)
        return data_dict