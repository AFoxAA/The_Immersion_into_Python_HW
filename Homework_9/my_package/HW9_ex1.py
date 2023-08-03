import csv
import json
import random
import cmath
from functools import wraps
from typing import Callable, List, Dict, Union, Tuple

MIN_ROWS: int = 100
MAX_ROWS: int = 1001
MIN_NUMBER: int = -10
MAX_NUMBER: int = 11


def generate_random_numbers_csv(file_name: str) -> None:
    """
    Функция для генерации файла CSV со случайными числами
    """

    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        num_rows_to_generate: int = random.randint(MIN_ROWS, MAX_ROWS)
        for _ in range(num_rows_to_generate):
            num: List[int] = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(3)]
            csv_writer.writerow(num)


def get_quadratic_roots_report(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(file_name: str) -> None:
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            results = [{
                "Коэффициент a": a,
                "Коэффициент b": b,
                "Коэффициент c": c,
                "Корни уравнения": func(a, b, c)
            } for a, b, c in map(lambda row: map(int, row), csv_reader)]

        with open("Task_1.json", "w", encoding='utf-8') as file:
            json.dump(results, file, ensure_ascii=False, indent=4)

    return wrapper


def received_result_to_json_format(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        def decode_complex_number(complex_number: complex) -> Dict[str, Union[float, int]]:
            if isinstance(complex_number, complex):
                return {"Вещественная часть": complex_number.real, "Мнимая часть": complex_number.imag}

        json_result = {
            "x_1": decode_complex_number(result[0]) if isinstance(result[0], complex) else result[0],
            "x_2": decode_complex_number(result[1]) if isinstance(result[1], complex) else result[1]
        } if isinstance(result, tuple) else {"x1": result}
        return json_result

    return wrapper


@get_quadratic_roots_report
@received_result_to_json_format
def calculate_quadratic_roots(a: int, b: int, c: int) -> Tuple[float, float]:
    """
    Функция для вычисления корней квадратного уравнения.
    """
    if a == 0:
        return None
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        complex_root_1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        complex_root_2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return complex_root_1, complex_root_2

    elif discriminant == 0:
        root = -b / (2 * a)
        return root

    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
