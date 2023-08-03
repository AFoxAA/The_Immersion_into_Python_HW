from random import randint


def guess_num(min_num: int, max_num: int, counts: int) -> bool:

    """
    Функция для угадывания числа.

    """

    number: int = randint(min_num, max_num)
    print(f'Загаданное число: {number}')

    for _ in range(counts):
        current_num: int = int(input(f'Введите число от {min_num} до {max_num}: '))

        if current_num < number:
            print(f'Загаданное число больше этого')
        elif current_num > number:
            print(f'Загаданное число меньше этого')
        else:
            print('Вы угадали!')
            return True

    print(f'Попытки закончились, вы не угадали число {number}!')
    return False
