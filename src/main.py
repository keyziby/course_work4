from course_work4.config import OPERATIONS_PATH
from utils import number_format, date_format, get_data, get_sorted_list, get_filtered_data

data_dict = get_data(OPERATIONS_PATH)
date_list = get_filtered_data(data_dict)
sorted_list = get_sorted_list(date_list)


def make_list_operations():
    for i in range(5):
        for data in data_dict:
            if "from" not in data:
                continue
            elif data["date"][0:10] == sorted_list[i]:
                date_name = data["date"][0:10]
                description_name = data["description"]
                from_name = data["from"]
                to_name = data["to"]
                amount = data["operationAmount"]["amount"]
                currency = data["operationAmount"]["currency"]["name"]

                print(f"{date_format(date_name)} {description_name}\n"
                      f"{number_format(from_name)} -> {number_format(to_name)}\n"
                      f"{amount} {currency}\n"
                      f"")


make_list_operations()
