import csv
import pickle

def read_csv_to_pickle(csv_path: str) -> bytes:

    """
    Функция считывает данные из файла в формате CSV
    и преобразует их в байтовый формат с использованием модуля pickle
    """

    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_data = []

        next(csv_reader)

        for row in csv_reader:
            csv_data.append(row)

    pickle_data = pickle.dumps(csv_data)
    return pickle_data
