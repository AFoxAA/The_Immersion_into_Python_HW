import json
import os
from random import randint
from typing import Callable, List, Any, Dict

MIN_NUM: int = 1
MAX_NUM: int = 100
MIN_COUNT: int = 1
MAX_COUNT: int = 10


def repeat_call(num_repeats: int = 1):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            repeated_results: List[int] = [func(*args, **kwargs) for _ in range(num_repeats)]
            return repeated_results

        return wrapper

    return decorator


def check_parametr(func: Callable) -> Callable:
    def wrapper(number: int, count: int, *args: Any, **kwargs: Any) -> Any:
        if number > MAX_NUM or number < MIN_NUM:
            number = randint(MIN_NUM, MAX_NUM)
            print(f'\nСлучайное число = {number}\n')

        if count > MAX_COUNT or count < MIN_COUNT:
            count = randint(MIN_COUNT, MAX_COUNT)

        result: Any = func(number, count, *args, **kwargs)

        return result

    return wrapper


def logger(file_name: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                data: List[Dict[str, Any]] = json.load(f)
        else:
            data: List[Dict[str, Any]] = []

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal data
            json_dict: Dict[str, Any] = {'Аргументы': args, **kwargs}
            result: Any = func(*args, **kwargs)
            json_dict['Результат'] = result
            data.append(json_dict)

            with open(file_name, 'w', encoding='utf-8') as f1:
                json.dump(data, f1, ensure_ascii=False, indent=4)

            return result

        return wrapper

    return decorator


@repeat_call(3)
@check_parametr
@logger('Task_5_Seminar.json')
def guess_number_ex5(number: int, count: int) -> str:
    """
    Функция принимает на вход загаданное число и максимальное количество попыток.

    """

    for i in range(1, count + 1):
        print(f'Попытка № {i}. Осталось попыток: {count - i + 1}')

        num_input: int = int(input('Введите число: '))

        if num_input == number:
            return 'Вы угадали!'
        elif num_input < number:
            print('Ваше число меньше!')
        else:
            print('Ваше число больше!')

    return 'Вы не угадали!'
