def select_items(things: dict[str, float], payload_capacity: float) -> dict[str, float]:
    items_in_backpack: dict[str, float] = {}
    remaining_payload_capacity: float = payload_capacity

    sorted_items: list[tuple[str, float]] = sorted(things.items(), key=sort_by_mass)

    for thing, mass in sorted_items:
        if mass <= remaining_payload_capacity:
            items_in_backpack[thing] = mass
            remaining_payload_capacity -= mass

    return items_in_backpack

def sort_by_mass(item: tuple[str, float]) -> float:
    return item[1]

def __main():
    things: dict[str, float] = {
        'Палатка': 4,
        'Спальный мешок': 2,
        'Ложка': 0.5,
        'Чашка': 1,
        'Термос': 3
    }

    maximum_payload_capacity: float = 8

    items_in_backpack: dict[str, float] = select_items(things, maximum_payload_capacity)

    print("Выбранные вещи:")
    for thing, mass in items_in_backpack.items():
        print(thing, "-", mass)
        
if __name__ == '__main__':
    __main()
