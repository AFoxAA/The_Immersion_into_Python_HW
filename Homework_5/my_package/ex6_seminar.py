from typing import Generator

def generate_multiplication_table() -> Generator[int, None, None]:
    
    """
    Генератор для создания таблицы умножения в заданном диапазоне.

    :Возвращаемое значение:
        - Generator[str, None, None]: Итератор, возвращающий строки таблицы умножения по одной по мере генерации.
    """
    
    min_num: int = 2
    max_num: int = 10
    columns: int = 4
    align_width: int = 2
    
    multiplication_table = (f'{num3:>{align_width}} X {num2:>{align_width}} = {(num2 * num3):>{align_width}}\t' if num3 != num1 + columns - 1 
                            else f'{num3:>{align_width}} X {num2:>{align_width}} = {(num2 * num3):>{align_width}}\n' if num2 != max_num
                            else f'{num3:>{align_width}} X {num2:>{align_width}} = {(num2 * num3):>{align_width}}\n\n'
                            for num1 in range(min_num, max_num, columns)
                            for num2 in range(min_num, max_num + 1)
                            for num3 in range(num1, num1 + columns))
    
    return multiplication_table


__all__ = ['generate_multiplication_table']
