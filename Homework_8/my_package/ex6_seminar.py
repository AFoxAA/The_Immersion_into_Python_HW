import pickle
import csv


def converter_pickle_to_csv(pickle_file_path: str, csv_file_path: str) -> None:

    """
    Функция преобразует файлы pickle в файлы формата CSV
    """

    with open(pickle_file_path, 'rb') as file:
        pickle_data = pickle.load(file)

    with open(csv_file_path, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['level', 'id', 'name', 'hash'])

        for item in pickle_data:
            for level_key, values_list in item.items():
                for value in values_list:
                    user_id, user_name = list(value.items())[0]
                    hash_value_str: str = value['hash']
                    csv_writer.writerow([level_key, user_id, user_name, hash_value_str])