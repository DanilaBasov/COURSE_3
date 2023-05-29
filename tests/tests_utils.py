from utils.utils import get_last_dates, get_format_date, open_file_json, sort_filtered_date
import pytest

def test_open_file_json():
    date = open_file_json()
    assert isinstance(date, list)

def test_sort_filtered_date(test_date):
    assert sort_filtered_date(test_date[:2]) == [{"date": "2019-08-26T10:50:58.294041",
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "id": 441945886,
         "operationAmount": {"amount": "31957.58",
                             "currency": {"name": "руб.", "code": "RUB"}},
        "state": "EXECUTED",
        "to": "Счет 64686473678894779589"},]
    assert sort_filtered_date(test_date[:2], filtered_data_from=True) == [
        {'date': '2019-08-26T10:50:58.294041',
         'description': 'Перевод организации',
         'from': 'Maestro 1596837868705199',
         'id': 441945886,
         'operationAmount': {'amount': '31957.58',
                             'currency': {'code': 'RUB','name': 'руб.'}},
         'state': 'EXECUTED',
         'to': 'Счет 64686473678894779589'},
           ]
def test_get_last_dates(test_date):
    date = get_last_dates(test_date)
    assert [i["date"] for i in date] == ["2019-12-07T06:17:14.634890", "2019-08-26T10:50:58.294041",
                                         "2019-07-03T18:35:29.512364","2018-08-06T16:22:54.643491",
                                         "2018-06-30T02:08:58.425572"]

def test_get_format_date(test_date):
    date = get_format_date(test_date)
    assert date == [
           '07,12,2019 Перевод организации\n'
           'Visa Classic 2842 87** **** 9012 -> Счет **3655\n'
           '48150.39 USD',
           '26,08,2019 Перевод организации\n'
           'Maestro 1596 83** **** 5199 -> Счет **9589\n'
           '31957.58 руб.',
           '03,07,2019 Перевод организации\n'
           'MasterCard 7158 30** **** 6758 -> Счет **5560\n'
           '8221.37 USD',
           '30,06,2018 Перевод организации\n'
           'Счет 7510 68** **** 6952 -> Счет **6702\n'
           '9824.07 USD',
           '06,08,2018 Открытие вклада\n'
           ',   -> Счет **5758\n'
           '82946.19 руб.',
           ]