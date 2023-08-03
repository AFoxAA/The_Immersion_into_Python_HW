from typing import Dict, List

__result: Dict[str, int] = {}


def guessing(text: str, variants: list[str], counts: int) -> int:
    print(f'Отгадай загадку: {text}')

    for count in range(1, counts + 1):
        answer = input(f'Попытка № {count}. Введите отгадку: ')

        if answer in variants:
            print(f'Вы угадали за {count} попыток\n')
            return count

    print(f'Вы не угадали за {count} попыток!\n')
    return 0


def guesses_dict(riddles: Dict[str, List[str]], count: int) -> None:
    """
    Функция принимает словарь загадок и их возможных ответов, а затем предлагает пользователям угадать ответы на каждую загадку.
    """

    for key, value in riddles.items():
        res: int = guessing(key, value, count)
        __result_score(key, res)

    __printing_statistic()


def __result_score(text: str, count: int) -> None:
    __result.update({text: count})


def __printing_statistic() -> None:
    statistic: str = '\n'.join(
        f'Загадка: "{key}": использовано попыток - {value}' if value > 0
        else f'Загадка: "{key}": вы не угадали загадку'
        for key, value in __result.items()
    )
    print(f'Статистика:\n{statistic}')
