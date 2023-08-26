import json
from typing import Any


class UserData:
    def __init__(self, name: str, user_id: int, level: int) -> None:
        self.name: str = name
        self.user_id: int = user_id
        self.level: int = level

    def __str__(self) -> str:
        return f'level: {self.level}, id: {self.user_id}, name: {self.name}'

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))


def data_from_json(file_name: str) -> set[UserData]:
    with open(file_name, encoding='utf-8') as json_f:
        user_dict: Any = json.load(json_f)

    users = set()

    for level, user_data in user_dict.items():
        for user_id, name in user_data.items():
            users.add(UserData(name, int(user_id), int(level)))

    return users


if __name__ == "__main__":
    users_set = data_from_json('Task_4.json')

    for item in users_set:
        print(item)
