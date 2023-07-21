from typing import List, Tuple

def queens_no_collisions(queens: List[Tuple[int, int]]) -> bool:
    
    """
    Проверяет, есть ли столкновения между ферзями на шахматной доске.
    
    :Аргументы:
        - queens (List[Tuple[int, int]]): Список координат ферзей на шахматной доске.
        
    :Возвращаемое значение:
        - bool: True, если ферзи не сталкиваются, иначе False.
    """
    
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if (queens[i][0] == queens[j][0] or  # Проверка по горизонтали
                    queens[i][1] == queens[j][1] or  # Проверка по вертикали
                    abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1])):  # Проверка по диагоналям
                return False
    return True

__all__ = ['queens_no_collisions']
