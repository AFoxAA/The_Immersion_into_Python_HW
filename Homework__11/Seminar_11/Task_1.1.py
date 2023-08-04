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
        instance.time_created = time()
        print(f'Создал класс: {cls}')
        return instance


if __name__ == '__main__':
    new_str: My_string = My_string('Тест строки', 'New Name')
    print(new_str.author_name)
    print(new_str.time_created)

    print(My_string.__doc__)
    print(My_string.__new__.__doc__)
