import os
import json
import csv
import pickle
from typing import List, Dict, Any


def collect_directory_info(directory_path: str) -> None:

    """
    Функция принимает путь к директории в качестве входного аргумента
    и обрабатывает все файлы и поддиректории внутри этой директории
    """

    directory_info_list: List[Dict[str, Any]] = []
    total_size_bytes: int = 0

    for root_path, subdirectories, files in os.walk(directory_path):
        for file in files:
            file_path: str = os.path.join(root_path, file)
            file_size_bytes: int = os.path.getsize(file_path)
            directory_info_list.append({
                'path': file_path,
                'type': 'file',
                'parent_directory': os.path.dirname(file_path),
                'size': file_size_bytes,
            })
            total_size_bytes += file_size_bytes

        for subdirectory_name in subdirectories:
            subdirectory_path: str = os.path.join(root_path, subdirectory_name)
            subdirectory_size_bytes: int = calculate_directory_size(subdirectory_path)
            directory_info_list.append({
                'path': subdirectory_path,
                'type': 'directory',
                'parent_directory': os.path.dirname(subdirectory_path),
                'size': subdirectory_size_bytes
            })
            total_size_bytes += subdirectory_size_bytes

    save_to_json(directory_info_list, 'HW8_1.json')
    save_to_csv(directory_info_list, 'HW8_1.csv')
    save_to_pickle(directory_info_list, 'HW8_1.pickle')


def calculate_directory_size(directory_path: str) -> int:

    """
    Функция вычисляет общий размер директории и всех её поддиректорий
    """

    total_size_bytes: int = 0

    for root_path, _, files in os.walk(directory_path):
        for file in files:
            file_path: str = os.path.join(root_path, file)
            total_size_bytes += os.path.getsize(file_path)

    return total_size_bytes


def save_to_json(data_list: List[Dict[str, Any]], file_name: str) -> None:

    """
    Функция сохраняет данные в формате JSON
    """

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4, ensure_ascii=False)


def save_to_csv(data_list: List[Dict[str, Any]], file_name: str) -> None:

    """
    Функция сохраняет данные в формате CSV
    """

    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['path', 'type', 'parent_directory', 'size'])
        for item in data_list:
            csv_writer.writerow([item['path'], item['type'], item['parent_directory'], item['size']])


def save_to_pickle(data_list: List[Dict[str, Any]], file_name: str) -> None:

    """
    Функция сохраняет данные в формате PICKLE
    """

    with open(file_name, 'wb') as pickle_file:
        pickle.dump(data_list, pickle_file)
