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


def get_sorted_list(date_list):
    sorted_list = sorted(date_list, reverse=True)[0:5]
    return sorted_list


def number_format(name):
    if "счет" in name.lower():
        name_list = name.split()
        format_number = name_list[0] + " " + "**" + name_list[-1][-4:]
        return format_number
    else:
        name_list = name.split()
        name_operation = name_list[0:-1]
        format_number = " ".join(name_operation) + " " + name_list[-1][0:4] + " " + name_list[-1][
                                                                                    4:6] + "**" + " " + "****" + " " + \
                        name_list[-1][-4:]
        return format_number


def date_format(date):
    format_date = ".".join(date.split("-")[::-1])
    return format_date
