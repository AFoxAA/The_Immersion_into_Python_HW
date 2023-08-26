class RectangleRanges:
    def __set_name__(self, owner, name):
        self.param_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Значение должно быть положительным')
        setattr(instance, self.param_name, value)


class Rectangle:
    _width = RectangleRanges()
    _height = RectangleRanges()

    def __init__(self, width: float, height: float = None):
        self._width = width

        if height is None:
            self._height = width
        else:
            self._height = height

    def calc_perimeter(self):
        return 2 * (self._width + self._height)

    def calc_area(self):
        return self._width * self._height

    def __add__(self, other):
        perimeter: float = self.calc_perimeter() + other.calc_perimeter()
        width: float = self._width + other.width
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        width: float = abs(self._width - other.width)
        perimeter: float = abs(self.calc_perimeter() - other.calc_perimeter())
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self) -> str:
        return f'\nПериметр = {self.calc_perimeter()}\nШирина = {self._width}\nДлина = {self._height}\n'

    def __eq__(self, other) -> bool:
        return self.calc_area() == other.calc_area()

    def __lt__(self, other) -> bool:
        return self.calc_area() < other.calc_area()

    def __le__(self, other) -> bool:
        return self.calc_area() <= other.calc_area()


if __name__ == '__main__':
    rect = Rectangle(5, 20)
    print(rect)
