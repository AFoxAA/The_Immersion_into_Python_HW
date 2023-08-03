from Homework_9.my_package import guesses_dict
from typing import Dict, List

MAX_ATTEMPTS: int = 3


def main() -> None:
    riddles_and_nswers: Dict[str, List[str]] = {
        'Лёгонькое, маленькое, а на крышу не закинешь?': ['Перо', 'Пёрышко', 'перо', 'пёрышко'],
        'Что можно встретить один раз в минуту, два раза в моменте и ни разу в тысяче лет?': ['Букву М', 'Буква М', 'М',
                                                                                              'м'],
        'Красна девица сидит в темнице, а коса на улице?': ['Морковь', 'Морковка', 'морковь', 'морковка'],
        'Жидкое, а не вода, белое, а не снег': ['Молоко', 'молоко', 'Молочко', 'молочко']}

    guesses_dict(riddles_and_nswers, MAX_ATTEMPTS)


if __name__ == '__main__':
    main()
