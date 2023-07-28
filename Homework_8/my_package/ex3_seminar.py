import json
import csv


def convert_json_to_csv(json_file_path: str, csv_file_path: str) -> None:
    """
    Функция преобразует данные из файла в формате JSON в файл формата CSV.
    """

    with open(json_file_path, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)

    with open(csv_file_path, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['level', 'id', 'name'])

        for item in data_dict:
            for level_key, values_dict in item.items():
                for id_key, name_value in values_dict.items():
                    csv_writer.writerow([level_key, id_key, name_value])
