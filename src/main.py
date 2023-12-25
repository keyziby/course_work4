import json

def get_data(path):
    with open(path, encoding='utf-8') as f:
        data_dict = json.load(f)
        return data_dict
def get_filtered_data(data_dict):
    date_list = []
    for data in data_dict:
        if "from" not in data:
            continue
        elif data["state"] == "EXECUTED":
            date_list.append(data["date"][0:10])
    return date_list