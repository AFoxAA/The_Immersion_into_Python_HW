from Homework_8.my_package import converter_pickle_to_csv


def main() -> None:
    pickle_file: str = '../Task_5_Seminar/Task_5_seminar_8.pickle'
    csv_file: str = 'Task_6_Seminar_8.csv'

    converter_pickle_to_csv(pickle_file, csv_file)


if __name__ == '__main__':
    main()
