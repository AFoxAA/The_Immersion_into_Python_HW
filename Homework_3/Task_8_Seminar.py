friends: dict[str, tuple] = {
    'Друг1': ('Рюкзак', 'Палатка', 'Ложка', 'Чашка'),
    'Друг2': ('Рюкзак', 'Ложка', 'Спички', 'Фанарик', 'Вилка'),
    'Друг3': ('Рюкзак', 'Чашка', 'Термос', 'Компас', 'Вилка'),
}

common_items: set[str] = set(friends['Друг1'])
missing_items: dict[str, set[str]] = {}

for friend in friends:
    common_items = common_items.intersection(set(friends[friend]))

unique_items: set[str] = set()
all_items: set[str] = set()

for items in friends.values():
    for item in items:
        if item in all_items:
            unique_items.discard(item)
        else:
            all_items.add(item)
            unique_items.add(item)

print(f'\nВещи взятые всеми тремя друзьями: {common_items}')
print(f'Уникальные вещи, которые есть только у одного друга: {unique_items}\n')
            
for friend, items in friends.items():
    for item in items:
        if item not in common_items:
            if item not in missing_items:
                missing_items[item] = set()
            missing_items[item].add(friend)
            
print('Вещи, которые есть у всех друзей кроме одного и имя друга:')
for item, friends_set in missing_items.items():
    if len(friends_set) == len(friends) - 1:
        missing_friend = (set(friends.keys()) - friends_set).pop()
        print(f'{item}: {missing_friend}')