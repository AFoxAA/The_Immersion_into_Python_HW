num = int(input('Введите число от 0 до 100 000: '))

if num < 0 or num > 100000:
    print('Вы ввели недопустимое значение ')
else:
    if num < 2:
        print(f'Число {num} не является ни простым, ни составным')
    else:
        prime_num = 1

        for i in range(2, num):
            if num % i == 0:
                prime_num = 0
                break

        if prime_num == 1:
            print(f'Число {num} является простым')
        else:
            print(f'Число {num} является составным')
