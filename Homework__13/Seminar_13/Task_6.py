class MyExClass(Exception):
    pass


class MyLevelEx(MyExClass):
    def __init__(self, user_name: str, user_level: int, admin_level: int):
        self.user_name: str = user_name
        self.user_level: int = user_level
        self.admin_level: int = admin_level

    def __str__(self) -> str:
        return f'Уровень доступа пользователя {self.user_name} = {self.user_level}, ' \
               f'ниже уровня доступа администратора = {self.admin_level}\nДоступ запрещен!'


class MyAccessEx(MyExClass):
    def __init__(self, user_id: int, user_name: str):
        self.user_id: int = user_id
        self.user_name: str = user_name

    def __str__(self) -> str:
        return f'Пользователь с именем: {self.user_name} и id: {self.user_id} отсутствует в системе!\nДоступ запрещен!'
