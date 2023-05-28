from utils.utils import open_file_json, sort_filtered_date, get_last_dates, get_format_date


def main():
    """
    основной код программы обьеденяющий функции"
    """

    Filtered_Data_From = True

    date = open_file_json()

    date = sort_filtered_date(date, filtered_data_from=Filtered_Data_From)
    date = get_last_dates(date)
    date = get_format_date(date)
    print("INFO: Вывод транзакций...")
    for i in date:
        print(i, end="\n\n")
if __name__ == "__main__":
    main()

