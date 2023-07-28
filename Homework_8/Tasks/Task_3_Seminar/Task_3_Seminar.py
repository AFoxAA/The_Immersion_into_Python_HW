from Homework_8.my_package import convert_json_to_csv


def main() -> None:
    json_file_path: str = 'Task_3_seminar_8.json'
    csv_file_path: str = 'Task_3_seminar_8.csv'
    convert_json_to_csv(json_file_path, csv_file_path)


if __name__ == '__main__':
    main()
