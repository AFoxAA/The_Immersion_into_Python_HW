from typing import Dict, List

def bonus_сalculation(names: List[str], rates: List[str], bonus: List[str]) -> Dict[str, float]:
    
    """
    Функция вычисляет сумму бонуса для каждого имени сотрудника на основе их ставок и процентов бонуса.

    :Аргументы:
        - names (List[str]): Список имен.
        - rates (List[int]): Список ставок для каждого имени.
        - bonus (List[str]): Список процентов бонуса для каждого имени в формате "X.YZ%".
                           Пример: ["6.55%", "4.25%", "5.70%"].

    :Возвращаемое значение:
        - Dict[str, float]: Словарь, где ключами являются имена сотрудников, а значениями - суммы бонусов в формате float.
    """
    
    result = {names[i]: rates[i] * float(bonus[i].strip('%')) / 100 for i in range(len(names))}
    return result

__all__ = ['bonus_сalculation']
