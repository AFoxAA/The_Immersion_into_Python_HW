from random import shuffle
from typing import List

number_arrangements: int = 4
board_size: int = 8

def __solution_to_the_queens_problem(row: int, queens: List[int], arrangements: List[List[int]]) -> None:
    
    """
    Функция решает задачу о размещении ферзей на шахматной доске таким образом,
    чтобы они не били друг друга.
    
    :Аргументы:
        - row (int): Текущая строка для размещения ферзя.
        - queens List[int]: Список, содержащий текущую конфигурацию ферзей.
        - arrangements (List[List[int]]): Список, в который добавляются успешные конфигурации ферзей.
    :Возвращаемое значение:
        - None
    """
    
    if row == board_size:
        arrangements.append(queens.copy())
        return

    for col in range(board_size):
        queens[row] = col
        if __is_queen_placement_valid(queens, row):
            __solution_to_the_queens_problem(row + 1, queens, arrangements)

def __is_queen_placement_valid(queens: List[int], row: int) -> bool:
    
    """
    Функция проверяет, является ли текущая конфигурация ферзей допустимой.
    
    :Аргументы:
        - queens (List[int]): Список, содержащий текущую конфигурацию ферзей.
        - row (int): Текущая строка для проверки.
    
    :Возвращаемое значение: 
        - True, если текущая конфигурация допустима, иначе False.
    """
    
    for i in range(row):
        if queens[i] == queens[row] or \
           queens[i] - queens[row] == row - i or \
           queens[i] - queens[row] == i - row:
            return False
    return True

def calculate_successful_queen_placements() -> list[list[int]]:
    
    """
    Функция возвращает указанное количество успешных конфигураций ферзей.
    
    :Аргументы:
        - Нет аргументов.
    
    :Возвращаемое значение: 
        - List[List[Tuple[int, int]]]: Список успешных конфигураций ферзей
    """
    
    successful = []
    queens = [0] * board_size
    all_arrangements = []
    __solution_to_the_queens_problem(0, queens, all_arrangements)
    shuffle(all_arrangements)
    
    for i in range(min(number_arrangements, len(all_arrangements))):
        successful.append([(j + 1, all_arrangements[i][j] + 1) for j in range(board_size)])

    return successful

__all__ = ['calculate_successful_queen_placements']