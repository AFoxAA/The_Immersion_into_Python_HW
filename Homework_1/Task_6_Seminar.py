GREGORIAN_CALENDAR = 1582
MULTIPLE_400 = 400
MULTIPLE_100 = 100
MULTIPLE_4 = 4
STARTING_POINT = 1

result = ''
user_input = '\nВведите год: '

while True:
    year = int(input(user_input))

    if year < STARTING_POINT:
        user_input = f'Вы указали несуществующий год!' \
                     f'\n\nВведите год: '
    
    elif year < GREGORIAN_CALENDAR:
        if year % MULTIPLE_4 == 0:
            result = f'{year} - високосный год'
        else:
            result = f'{year} - невисокосный год'
        break
    
    else:
        if year % MULTIPLE_400 == 0:
            result = f'{year} - високосный год'
        elif year % MULTIPLE_100 == 0:
            result = f'{year} - невисокосный год'
        elif year % MULTIPLE_4 == 0:
            result = f'{year} - високосный год'
        else:
            result = f'{year} - невисокосный год'
        break
    
print(result)
