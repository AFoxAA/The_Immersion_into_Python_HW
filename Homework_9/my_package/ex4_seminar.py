from typing import Callable, List, Tuple, Dict, Any


def repeat_call(num_repeats: int = 1):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            repeated_results: List[int] = [func(*args, **kwargs) for _ in range(num_repeats)]
            return repeated_results

        return wrapper

    return decorator


@repeat_call(num_repeats=3)
def calculate_sum(first_num: int, second_num: int, *args: Tuple, **kwargs: Dict[str, Any]) -> int:
    """
    Функция вычисляет сумму двух чисел (first_num и second_num) типа int
    """

    sum_result: int = first_num + second_num
    return sum_result
