from Homework_8.my_package import csv_to_json_with_hashes


def main() -> None:
    input_file: str = '../Task_3_Seminar/Task_3_seminar_8.csv'
    output_file: str = 'Task_4_seminar_8.json'
    csv_to_json_with_hashes(input_file, output_file)


if __name__ == '__main__':
    main()
