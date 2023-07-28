import os
import json
import pickle


def convert_json_to_pickle(directory_path: str) -> None:

    """
    Функция преобразует файлы JSON в файлы формата Pickle
    """

    if not os.path.exists(directory_path):
        print(f'\n{directory_path} - такой директории не существует!')
        return

    json_files_list: list[str] = [file for file in os.listdir(directory_path) if file.endswith('.json')]

    for json_file in json_files_list:
        json_file_path: str = os.path.join(directory_path, json_file)
        pickle_file_name: str = 'Task_5_seminar_8.pickle'

        with open(json_file_path, 'r', encoding='utf-8') as file:
            json_data: dict = json.load(file)

        with open(pickle_file_name, 'wb') as file:
            pickle.dump(json_data, file)