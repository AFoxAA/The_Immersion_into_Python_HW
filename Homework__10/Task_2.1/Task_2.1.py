import os
import json
import csv
import pickle
from dotenv import load_dotenv


class FileNotFoundError(Exception):
    def __str__(self):
        return "\nУказанная директория не существует!"


class DirectoryProcessor:

    def __init__(self, directory):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.directory = os.path.join(script_directory, directory)
        self.result = []
        self.total_size = 0

    def process(self):
        if not os.path.exists(self.directory):
            raise FileNotFoundError

        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                self.result.append(self.get_item_data(file_path, 'file', file_size))
                self.total_size += file_size

            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                dir_size = self.get_directory_size(dir_path)
                self.result.append(self.get_item_data(dir_path, 'directory', dir_size))
                self.total_size += dir_size

        self.save_json()
        self.save_csv()
        self.save_pickle()

    def get_item_data(self, item_path, item_type, item_size):
        path = item_path.replace(self.directory, '').strip(os.path.sep)
        parent_dir = os.path.dirname(path)
        return {
            'path': path,
            'type': item_type,
            'parent_directory': parent_dir,
            'size': item_size
        }

    def get_directory_size(self, directory):
        total_size = 0
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
        return total_size

    def save_json(self):
        file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Task_2.1.json')
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(self.result, json_file, ensure_ascii=False, indent=4)

    def save_csv(self):
        file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Task_2.1.csv')
        with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['path', 'type', 'parent_directory', 'size'])
            for item in self.result:
                writer.writerow([item['path'], item['type'], item['parent_directory'], item['size']])

    def save_pickle(self):
        file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Task_2.1.pickle')
        with open(file_name, 'wb') as pickle_file:
            pickle.dump(self.result, pickle_file)


if __name__ == '__main__':
    try:
        load_dotenv()
        processor = DirectoryProcessor(os.getenv('YOUR_DIRECTORY'))
        processor.process()
    except (FileNotFoundError) as e:
        print(f"\nОшибка: {e}")
