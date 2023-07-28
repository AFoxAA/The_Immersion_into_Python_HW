import csv
import json
from typing import List, Union


def csv_to_json_with_hashes(csv_file_path: str, json_file_path: str) -> str:
    """
    Преобразует CSV-файл в JSON-формат и добавляет хэш для каждой строки
    """

    output_csv_file: str = 'Task_4_seminar_8.csv'

    data_dict: dict[str, list[dict[str, Union[str, int]]]] = {}

    with open(csv_file_path, 'r', encoding='utf-8') as in_file:
        csv_reader = csv.reader(in_file)
        headers: List[str] = next(csv_reader)

        with open(output_csv_file, 'w', newline='', encoding='utf-8') as out_file:
            csv_writer: csv._writer = csv.writer(out_file)
            csv_writer.writerow(headers + ['hash'])

            for row in csv_reader:
                level, id_num, name = row

                id_num_padded: str = id_num.zfill(10)
                name_lower: str = name.lower()

                hash_value: str = calculate_hash(name_lower, id_num_padded)
                data_dict.setdefault(level, []).append({id_num_padded: name_lower, 'hash': hash_value})
                csv_writer.writerow([level, id_num_padded, name_lower, hash_value])

    json_data = {}
    for level, rows in data_dict.items():
        json_data[level] = rows

    formatted_data = [{k: v} for k, v in json_data.items()]

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(formatted_data, json_file, ensure_ascii=False, indent=4)

    return output_csv_file


def calculate_hash(name: str, id_num: str) -> str:
    """
    Вычисляет хэш для комбинации имени и идентификатора
    """

    combined_string: int = hash(name) + hash(id_num)
    return str(combined_string)
