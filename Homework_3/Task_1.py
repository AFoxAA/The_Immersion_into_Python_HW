# Вариант через генератор
def duplicating_elements(elements: list[int]) -> list[int]:
    all_elements: set[int] = set()
    duplicates: set[int] = set(item for item in elements if item in all_elements or all_elements.add(item))
    return duplicates

elements: list[int] = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]
result: list[int] = list(duplicating_elements(elements))
print(result)


# Второй вариант
def duplicating_elements(elements: list[int]) -> list[int]:
    all_elements: set[int] = set()
    duplicates: set[int] = set()
    for item in elements:
        if item in all_elements:
            duplicates.add(item)
        else:
            all_elements.add(item)
    return duplicates

elements: list[int] = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]
result: list[int] = list(duplicating_elements(elements))
print(result)


# Третий вариант через словарь
def duplicating_elements(elements: list[int]) -> list[int]:
    num_dict: dict[int, int] = {}
    for i in elements:
        num_dict[i] = num_dict.get(i, 0) + 1

    new_list: list[int] = [key for key, value in num_dict.items() if value > 1]
    return new_list

elements: list[int] = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]
result: list[int] = duplicating_elements(elements)
print(result)
