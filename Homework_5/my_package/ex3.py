from typing import Generator

def fibonacci_numbers_generator() -> Generator[int, None, None]:
    
    """
    Генератор, который возвращает последовательность чисел Фибоначчи.

    :Возвращаемое значение:
        - Generator[int, None, None]: Итератор, возвращающий числа Фибоначчи по одному по мере генерации.
    """
    
    number_1: int = 0
    number_2: int = 1
    while True:
        yield number_1
        number_1, number_2 = number_2, number_1 + number_2


__all__ = ['bonus_сalculation']
