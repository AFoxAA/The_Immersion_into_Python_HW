from fractions import Fraction

# Ввод дробей
string_1: str = input("\n1. Введите первую дробь в формате a/b: ")
string_2: str = input("2. Введите вторую дробь в формате a/b: ")

# Получение числителя и знаменателя в виде числа
def get_num(string: str) -> tuple[int, int]:
    numerator, denominator = map(int, string.split('/'))
    return numerator, denominator

# Сложение двух дробей
def sum_fractions(frac_1: tuple[int, int], frac_2: tuple[int, int]) -> tuple[int, int]:
    numerator_1, denominator_1 = frac_1
    numerator_2, denominator_2 = frac_2
    result_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
    result_denominator = denominator_1 * denominator_2
    return result_numerator, result_denominator

# Перемножение двух дробей
def mult_fraction(frac_1: tuple[int, int], frac_2: tuple[int, int]) -> tuple[int, int]:
    numerator1, denominator1 = frac_1
    numerator2, denominator2 = frac_2
    result_numerator = numerator1 * numerator2
    result_denominator = denominator1 * denominator2
    return result_numerator, result_denominator

# Нахождение наибольшего общего делителя (Алгоритм Евклида)
def euclidean_algorithm(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Сокращение дроби до простейшего вида 
def reduce_fraction(fraction: tuple[int, int]) -> tuple[int, int]:
    numerator, denominator = fraction
    divisor_shared = euclidean_algorithm(numerator, denominator)
    reduced_numerator = numerator // divisor_shared
    reduced_denominator = denominator // divisor_shared
    return reduced_numerator, reduced_denominator

# Извлечение числителя и знаменателя
num_1: tuple[int, int] = get_num(string_1)
num_2: tuple[int, int] = get_num(string_2)

# Вывод итогового рузультат сложения двух дробей
sum_frac: tuple[int, int] = sum_fractions(num_1, num_2)
reduced_sum_frac: tuple[int, int] = reduce_fraction(sum_frac)
print("\n1. Сумма дробей:", '/'.join(map(str, reduced_sum_frac)))

# Вывод итогового рузультат перемножения двух дробей
mult_frac: tuple[int, int] = mult_fraction(num_1, num_2)
reduced_mult_frac: tuple[int, int] = reduce_fraction(mult_frac)
print("2. Произведение дробей:", '/'.join(map(str, reduced_mult_frac)))

# Проверка своего кода при помощи модуля fractions
print('\n\033[93m\033[4mПроверка через модуль Fractions\033[0m')
print(f'1. Проверка результата первой дроби при помощи fractions: {Fraction(string_1) + Fraction(string_2)}')
print(f'2. Проверка результата второй дроби при помощи fractions: {Fraction(string_1) * Fraction(string_2)}')
