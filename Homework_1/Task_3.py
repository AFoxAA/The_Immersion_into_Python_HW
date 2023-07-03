from random import randint

num = randint(0, 1000)
initial_attempts = 10
counter = 1
used_attempts = 0

while counter <= 10:
    user_number = int(input('\nВведите число от 0 до 1000: '))

    if user_number < 0 or user_number > 1000:
        print(f'Число {user_number} не входит в диапазон чисел от 0 до 1000')

    else:
        used_attempts += 1

        if user_number == num:
            print(f'Вы угадали с {used_attempts} попытки!!!')
            break

        if user_number > num:
            print(f'Вводимое число больше {num}!!!')
        else:
            print(f'Вводимое число меньше {num}')
        counter += 1

if used_attempts == initial_attempts and user_number != num:
    print('\nПопытки закончились, вы не угадали число!!!')
