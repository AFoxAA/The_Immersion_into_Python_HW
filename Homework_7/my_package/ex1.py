import os


def create_new_files(files: int = 5) -> None:
    """
    Функция создает новые текстовые файлы в указанной директории
    """

    directory_for_saving: str = 'Переименованные файлы'

    os.makedirs(directory_for_saving, exist_ok=True)

    print('\n\033[93mНовые файлы:\033[0m')
    for i in range(files):
        new_file_name: str = f"New_file{i + 1}.txt"
        new_file_path: str = os.path.join(directory_for_saving, new_file_name)
        with open(new_file_path, 'w') as file:
            pass

        print(f'{new_file_name}')


def rename_files(new_name: str, init_ext: str, mod_ext: str, char_range: list[int],
                 num_digits: int = 5) -> None:

    """
    Функция переименовывает файлы с определенным расширением в указанной директории.
    """

    directory: str = 'Переименованные файлы'

    files_to_rename: list[str] = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files_to_rename = [f for f in files_to_rename if f.endswith(init_ext)]

    print('\n\033[93mИзмененные файлы:\033[0m')
    for i, file_name in enumerate(files_to_rename):
        file_count: str = str(i + 1).zfill(num_digits)
        file_name_slice: str = file_name[char_range[0] - 1: char_range[1]]
        new_file_name: str = file_name_slice + new_name + file_count + mod_ext

        while os.path.exists(os.path.join(directory, new_file_name)):
            i += 1
            file_count = str(i + 1).zfill(num_digits)
            new_file_name = file_name_slice + new_name + file_count + mod_ext

        old_file_path: str = os.path.join(directory, file_name)
        new_file_path: str = os.path.join(directory, new_file_name)
        os.rename(old_file_path, new_file_path)

        print(f'{file_name} -> {new_file_name}')
