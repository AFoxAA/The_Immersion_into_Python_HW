from Homework_8.my_package import read_csv_to_pickle


def main() -> None:
    csv_file: str = '../Task_6_Seminar/Task_6_Seminar_8.csv'
    pickle_data: bytes = read_csv_to_pickle(csv_file)
    print(pickle_data)


if __name__ == '__main__':
    main()
