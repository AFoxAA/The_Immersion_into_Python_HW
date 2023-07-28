from Homework_8.my_package import convert_json_to_pickle


def main() -> None:
    directory: str = '../Task_4_Seminar'
    convert_json_to_pickle(directory)


if __name__ == '__main__':
    main()
