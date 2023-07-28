import os
import random


def generate_files_with_extensions(addon_directory: str, excluded_files: list[str], file_count: int, min_num: int = 1,
                                   max_num: int = 101) -> None:

    """
    Функция создает заданное количество файлов с расширениями в указанной директории.
    """

    os.makedirs(addon_directory, exist_ok=True)
    for _ in range(file_count):
        extension: str = random.choice(excluded_files)
        random_filename: str = str(random.randint(min_num, max_num))
        file_path_with_extension: str = os.path.join(addon_directory, random_filename + extension)
        with open(file_path_with_extension, 'w'):
            pass


def sort_files_by_extension(essential_dirs: dict[str, list[str]], addon_directory: str, final_dir: str) -> None:

    """
    Функция сортирует файлы в указанной директории по расширениям и перемещает их в соответствующие директории
    """

    for file_group_name in essential_dirs.keys():
        group_directory_path: str = os.path.join(final_dir, file_group_name)
        os.makedirs(group_directory_path, exist_ok=True)

    sorted_files_info: list[tuple[str, str]] = []

    for filename in os.listdir(addon_directory):
        source_file_path: str = os.path.join(addon_directory, filename)

        if os.path.isfile(source_file_path):
            file_extension: str = os.path.splitext(filename)[1].lower()

            for file_group_name, extensions in essential_dirs.items():
                if file_extension in extensions:
                    destination_group_directory: str = os.path.join(final_dir, file_group_name)
                    destination_file_path: str = os.path.join(destination_group_directory, filename)

                    if os.path.exists(destination_file_path):
                        sorted_files_info.append((f"Файл '{filename}' был создан ранее", filename))
                    else:
                        os.rename(source_file_path, destination_file_path)
                        sorted_files_info.append((f"Файл '{filename}' создан успешно", filename))
                    break
            else:
                continue

    sorted_files_info: list[tuple[str, str]] = sorted(sorted_files_info, key=lambda x: x[1])

    for file_info in sorted_files_info:
        print(file_info[0])
