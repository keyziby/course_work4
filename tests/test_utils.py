import os

from config import ROOT_DIR
from src.utils import number_format, date_format, get_data, get_sorted_list, get_filtered_data


def test_number_format():
    assert number_format("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert number_format("Счет 35383033474447895560") == "Счет **5560"


def test_date_format():
    assert date_format("2018-06-30") == "30.06.2018"


def test_get_data():
    path = os.path.join(ROOT_DIR, "tests", "test_operation.json")
    assert get_data(path) == [1, 2, 3]


def test_get_sorted_list():
    data = ["2018-03-23", "2019-08-26", "2019-07-03", "2020-07-03", "2014-07-03"]
    assert get_sorted_list(data) == ["2020-07-03", "2019-08-26", "2019-07-03", "2018-03-23", "2014-07-03"]


def test_get_filtered_data():
    dictionary = [
        {
            "id": 441945886,
            "state": "CANCELLED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }]
    assert get_filtered_data(dictionary) == ["2019-07-03"]
