def select_items(things: dict[str, int], payload_capacity: int) -> list[list[str]]:
    remaining_payload_capacity: int = payload_capacity
    selected_combination: list[list[str]] = []   
    remaining_things: list[str] = list(things)
    
    for _ in range(len(remaining_things)):
    
        for  j in range(len(remaining_things)):
            
            current_mass: int = 0
            current_combination: list[str] = []
                
            for key in remaining_things:
                if things[key] + current_mass <= remaining_payload_capacity:
                    current_combination.append(key)
                    current_mass += things[key]
            
            current_combination.sort()
                        
            if current_combination not in selected_combination:
                selected_combination.append(current_combination)
               

            if (len(things) - 1) != j:
                remaining_things[j], remaining_things[j + 1] = remaining_things[j + 1], remaining_things[j] 
    return selected_combination
        
def __main() -> None:
    things: dict[str, float] = {
        'Палатка': 4,
        'Спальный мешок': 2,
        'Ложка': 0.5,
        'Чашка': 1,
        'Термос': 3
    }

    maximum_payload_capacity: float = 8
    items_in_backpack: list[list[str]] = select_items(things, maximum_payload_capacity)

    print("Выбранные вещи:")
    for i in range(len(items_in_backpack)):
        print(f'Вариант {i+1}: ', end='')
        new_str: list[str] = []
        for k in items_in_backpack[i]:
            new_str.append(f'{k} - {things[k]}')
        print(', '.join(new_str))   

if __name__ == '__main__':
    __main()

        
        