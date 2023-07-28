from random import randint, choices
from string import ascii_letters, digits


def generate_random_filename(ext: list[str], name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256,
                             bytes_max: int = 4096) -> None:
    """
       Генерирует случайное имя файла с указанным расширением и сохраняет его в формате бинарных данных (bytes).
    """

    name_length: int = randint(name_len_min, name_len_max)
    name: str = ''.join(choices(ascii_letters + digits, k=name_length))
    data: bytes = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))

    with open(f'{name}.{ext}', 'wb') as file:
        file.write(data)

    num_bytes: int = len(data)
    print(f"Создан файл '{name}.{ext}' размером {num_bytes} байт.")


def generate_multiple_files(ext: list[str], num_files: list[int], name_len_min: int = 6, name_len_max: int = 30,
                            bytes_min: int = 256, bytes_max: int = 4096) -> None:
    """
    Создает несколько файлов с заданными расширениями и случайными именами.
    """

    if len(ext) != len(num_files):
        print("Количество расширений и файлов должно совпадать!")
        return

    for ext, count in zip(ext, num_files):
        for _ in range(count):
            generate_random_filename(ext, name_len_min, name_len_max, bytes_min, bytes_max)
