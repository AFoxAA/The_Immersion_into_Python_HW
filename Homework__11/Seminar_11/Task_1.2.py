from typing import List


class Archieve:
    """
    Класс Archive представляет собой архивирование данных.
    """

    __instance: 'Archieve' = None

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
            cls.__instance.num_list: List[int] = []
            cls.__instance.text_list: List[str] = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance


if __name__ == '__main__':
    new_arch_1: Archieve = Archieve(1, 'test_1')

    new_arch_2: Archieve = Archieve(2, 'test_2')
    print(new_arch_2.num_list)
    print(new_arch_2.text_list)

    help(Archieve)
