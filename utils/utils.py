import json
from datetime import datetime


def open_file_json():
    """загрузка фойла json"""
    with open("operations.json", "r", encoding="UTF-8") as file:
        list_filt_data = json.load(file)
        return list_filt_data


def sort_filtered_date(list_filt_data, filtered_data_from=False):
    """
    фильтрует файл:
    1 на наличие исполнению опереации state
    2 на наличие операции from
    """
    list_filt_data = [dat for dat in list_filt_data if "state" in dat and dat["state"] == "EXECUTED"]
    if filtered_data_from:
        list_filt_data = [dat for dat in list_filt_data if "from" in dat]
    return list_filt_data


def get_last_dates(list_filt_data):
    """
    функуия сортирует по дате пять последних опраций
    """
    list_filt_data = sorted(list_filt_data, key=lambda dat: dat["date"], reverse=True)
    list_filt_data = list_filt_data[:5]
    return list_filt_data


def get_format_date(list_filt_data):
    """
    функция форматирует время в формат (день месяц год)
    переписывает сяет получателя в нужный формат
    переписывает счет отправителя в нужный формат
    переписывает информацию о переводе и суммуы перевода в валюте
    формирует новый список с измененным форматом данных
    """
    list_formatt_date = []
    for i in list_filt_data:
        list_filt_data = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d,%m,%Y")
        description = i["description"]
        recipient = f"{i['to'].split()[0]} **{i['to'][-4:]}"
        operation_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        if "from" in i:
            sender = i['from'].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
        else:
            from_info, from_bill = ", "
        list_formatt_date.append(f'''\
{list_filt_data} {description}
{from_info} {from_bill} -> {recipient}
{operation_amount}''')
    return list_formatt_date