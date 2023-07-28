from os import path, makedirs
from random import randint, choices
from string import ascii_letters, digits


def create_random_file(direct: str, ext: str, name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256,
                       bytes_max: int = 4096) -> None:
    """
    Генерирует случайное имя файла с указанным расширением и сохраняет его в формате бинарных данных (bytes).
    """

    name_length: int = randint(name_len_min, name_len_max)
    name: str = ''.join(choices(ascii_letters + digits, k=name_length))
    data: bytes = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
    file_path: str = path.join(direct, f'{name}.{ext}')

    if not path.exists(direct):
        makedirs(direct)

    if not path.exists(file_path):
        with open(file_path, 'wb') as file:
            file.write(data)
        num_bytes: int = len(data)
        print(f"Создан файл '{name}.{ext}' размером {num_bytes} байт.")
    else:
        print(f"Файл '{name}.{ext}' уже существует.")


def create_multiple_files(direct: str, ext: list[str], num_files: list[int], name_len_min: int = 6,
                          name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096) -> None:
    """
    Создает несколько файлов с заданными расширениями и случайными именами.
    """

    if len(ext) != len(num_files):
        print("Количество расширений и файлов должно совпадать!")
        return

    for ext, count in zip(ext, num_files):
        for _ in range(count):
            create_random_file(direct, ext, name_len_min, name_len_max, bytes_min, bytes_max)
