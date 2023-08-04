from typing import Union, Type


class Factory:
    def __init__(self, animal_class: Type[Union['Fish', 'Bird', 'Mammal']]) -> None:
        self.animal_class: Type[Union[Fish, Bird, Mammal]] = animal_class

    def create_fish(self, name: str, length: int, small_length_threshold: int, large_length_threshold: int) -> 'Fish':
        return Fish(name, length, small_length_threshold, large_length_threshold)

    def create_bird(self, name: str, wingspan: int) -> 'Bird':
        return Bird(name, wingspan)

    def create_mammal(self, name: str, fur_color: str, has_tail: bool) -> 'Mammal':
        return Mammal(name, fur_color, has_tail)


class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def display_special_feature(self) -> None:
        pass


class Fish(Animal):
    def __init__(self, name: str, length: int, small_length_threshold: int, large_length_threshold: int) -> None:
        super().__init__(name)
        self.length: int = length
        self.SMALL_LENGTH_THRESHOLD: int = small_length_threshold
        self.LARGE_LENGTH_THRESHOLD: int = large_length_threshold

    def display_special_feature(self) -> str:
        if self.length < self.SMALL_LENGTH_THRESHOLD:
            return 'Рыба небольшого размера'
        elif self.length > self.LARGE_LENGTH_THRESHOLD:
            return 'Рыба большого размера'
        else:
            return 'Рыба среднего размера'


class Bird(Animal):
    def __init__(self, name: str, wingspan: int) -> None:
        super().__init__(name)
        self.wingspan: int = wingspan

    def display_special_feature(self) -> str:
        return f'Размах крыльев: {self.wingspan * 2}'


class Mammal(Animal):
    def __init__(self, name: str, fur_color: str, has_tail: bool) -> None:
        super().__init__(name)
        self.fur_color: str = fur_color
        self.has_tail: bool = has_tail

    def display_special_feature(self) -> str:
        tail_info = "имеет хвост" if self.has_tail else "не имеет хвоста"
        return f'{self.name} - млекопитающее с {self.fur_color} окрасом и {tail_info}.'


if __name__ == '__main__':
    SMALL_LENGTH_THRESHOLD: int = 10
    LARGE_LENGTH_THRESHOLD: int = 100

    factory_fish: Factory = Factory(Fish)
    fish = factory_fish.create_fish('акула', 50, SMALL_LENGTH_THRESHOLD, LARGE_LENGTH_THRESHOLD)

    factory_bird: Factory = Factory(Bird)
    bird = factory_bird.create_bird('орел', 30)

    factory_mammal: Factory = Factory(Mammal)
    mammal = factory_mammal.create_mammal('Кит', 'черно-белым', True)

    print(fish.display_special_feature())
    print(bird.display_special_feature())
    print(mammal.display_special_feature())

