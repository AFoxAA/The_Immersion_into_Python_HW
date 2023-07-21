from re import match

min_date: int = 1
max_year: int = 9999
max_month: int = 12
max_day: int = 31
date_regex: str = r'^\d{2}\.\d{2}\.\d{4}$'

def valid_date(date: str) -> bool:
    
    """
    Функция проверяет, является ли введенная дата допустимой.

    :Аргументы:
        - date (str): Строка, содержащая дату в формате "дд.мм.гггг".

    :Возвращаемое значение:
        - bool: True, если дата допустима, иначе False.
    """
    
    if not match(date_regex, date):
        return False

    day, month, year = map(int, date.split('.'))
    
    if not (min_date <= year <= max_year and min_date <= month <= max_month and min_date <= day <= max_day):
        return False
    
    if month in (4, 6, 9, 11) and day > 30:
        return False
    
    if month == 2 and __leap_year(year) and day > 29:
        return False
    
    if month == 2 and not __leap_year(year) and day > 28:
        return False
    
    return True

def __leap_year(year: int) -> bool:
    
    """
    Функция проверяет, является ли год високосным.

    :Аргументы:
        - year (int): Год для проверки.

    :Возвращаемое значение:
        bool: True, если год високосный, иначе False.
    """
    
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

__all__ = ['valid_date']
