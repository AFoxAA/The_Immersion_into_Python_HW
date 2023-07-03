START_OF_THE_RANGE = 1
SQUARE_OF_A_NUMBER = 2
DIGIT = 10
TWO_DIGIT_NUMBER = 100
THREE_DIGIT_NUMBER = 1000

result = ''
user_input = '\nВведите число от 1 до 999: '


while True:
    number = int(input(user_input))

    if START_OF_THE_RANGE <= number < DIGIT:
        digit = number ** SQUARE_OF_A_NUMBER
        result = f'Вы ввели цифру. Квадрат числа {number} = {digit}'
        break

    elif DIGIT <= number < TWO_DIGIT_NUMBER:
        two_digit_1 = number // DIGIT
        two_digit_2 = number % DIGIT
        two_digit = two_digit_1 * two_digit_2
        result = f'Вы ввели двузначное число. Произведение цифр числа {number} = {two_digit}'
        break

    elif TWO_DIGIT_NUMBER <= number < THREE_DIGIT_NUMBER:
        three_digit_1 = number // TWO_DIGIT_NUMBER
        three_digit_2 = (number // DIGIT % DIGIT) * DIGIT
        three_digit_3 = (number % DIGIT) * TWO_DIGIT_NUMBER
        three_digit = three_digit_1 + three_digit_2 + three_digit_3
        result = f'Вы ввели трехзначное число. Зеркальное отображение числа {number} = {three_digit}'
        break

    else:
        user_input = f'Число {number} выходит за рамки диапазона. Повторите попытку!' \
                     f'\n\nВведите число от 1 до 999: '
        continue

print(result)