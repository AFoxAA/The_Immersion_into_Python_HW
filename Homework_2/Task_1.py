BINARY_SYSTEM = 2
OCTAL_SYSTEM = 8
HEXADECIMAL_SYSTEM = 16

number: int = int(input('\nВведите целое число: '))


def system_selection() -> int:
    system: int = 0

    while system != BINARY_SYSTEM and system != OCTAL_SYSTEM and system != HEXADECIMAL_SYSTEM:
        system = int(input('\nВыберите систему счисления\n'
                           '\n2 - двоичная система счисления'
                           '\n8 - восьмеричная система счисления'
                           '\n16 - шестнадцатеричная система счисления: '))
    return system


def transfer_to_the_system(number: int, system: int) -> str:
    result: str = ''

    while number != 0:
        mod: int = number % system
        
        if mod < 10:
            result = str(mod) + result
        else:
            result = chr(ord('a') + mod - 10) + result
        
        number //= system
        
    return result

selection: int = system_selection()
transfer: str = transfer_to_the_system(number, selection)

print(f'\nРезультат: {transfer}')

print(f'\nЧисло в двоичной системе счисления: {bin(number)[2:]}')
print(f'Число в восьмеричной системе счисления: {oct(number)[2:]}')
print(f'Число в шестнадцатеричной системе счисления: {hex(number)[2:]}')

