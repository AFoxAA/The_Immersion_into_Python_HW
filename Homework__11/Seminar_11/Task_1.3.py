from time import time


class My_string(str):
    """
    Класс представляет расширенную версию стандартного класса str.
    Он позволяет создавать объекты строк с дополнительными атрибутами, такими как имя автора и время создания.
    """

    def __new__(cls, value: str, author_name: str) -> 'My_string':
        """
        Создает новый экземпляр класса My_string с заданным значением и именем автора.
        """

        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_creared = time()
        print(f'Создал класс: {cls}')

        return instance


class Archieve():
    """
    Класс Archive представляет собой архивирование данных.
    """
    __instance = None

    def __init__(self, num: int, text: str) -> None:

        """
        Инициализирует новый экземпляр класса Archive с переданными числом и текстом.
        """

        self.text: str = text
        self.num: int = num

    def __new__(cls, *args, **kwargs) -> 'Archieve':

        """
        Возвращает единственный экземпляр класса Archive или создает новый, если еще не существует.
        """

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance


if __name__ == '__main__':
    print(f'\nЗадача 1:\n{My_string.__doc__}')
    print(f'Задача 2:\n{Archieve.__doc__}')
