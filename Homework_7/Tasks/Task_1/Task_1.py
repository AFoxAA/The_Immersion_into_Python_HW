from Homework_7.my_package import create_new_files, rename_files


def main() -> None:
    new_name_to_add: str = "_renamed_"
    initial_extension: str = ".txt"
    modified_extension: str = ".doc"
    character_range: list[int] = [5, 9]

    create_new_files()
    rename_files(new_name_to_add, initial_extension, modified_extension, character_range)


if __name__ == '__main__':
    main()
