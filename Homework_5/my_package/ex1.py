from typing import Tuple, List

def split_absolute_path(file_path: str) -> Tuple[str, str, str]:
    """
    Разделяет абсолютный путь на компоненты (путь, имя файла и расширение).

    :Аргументы:
        - file_path (str): Абсолютный путь к файлу.

    :Возвращаемое значение:
        - tuple[str, str, str]: Кортеж с тремя элементами: путь к файлу, имя файла и его расширение.
    """

    splitting_into_segments: List[str] = file_path.rsplit('/', 1)
    first_element_of_list: str = splitting_into_segments[0] if len(splitting_into_segments) > 1 else ''

    splitting_the_filename: List[str] = splitting_into_segments[-1].rsplit('.', 1)
    filename: str = splitting_the_filename[0]
    file_extension: str = '.' + splitting_the_filename[1] if len(splitting_the_filename) > 1 else ''

    result_tuple: Tuple[str, str, str] = (first_element_of_list, filename, file_extension)
    return result_tuple


__all__ = ['split_absolute_path']
