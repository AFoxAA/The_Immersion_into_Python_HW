class Rectangle:
    """
    Класс представляет прямоугольник и содержит методы для расчета его периметра и площади,
    а также для выполнения операций сложения и вычитания двух прямоугольников.
    """

    def __init__(self, width: float, height: float = None) -> None:

        """
        Метод инициализирует новый объект прямоугольника с указанными параметрами ширины и высоты.
        """

        self.width: float = width

        if height is None:
            self.height: float = width
        else:
            self.height: float = height

    def calc_perimeter(self) -> float:

        """
        Метод вычисляет периметр прямоугольника и возвращает его значение.
        """

        self.perimeter: float = (self.width + self.height) * 2
        return self.perimeter

    def calc_area(self) -> float:

        """
        Метод вычисляет площадь прямоугольника и возвращает её значение.
        """

        self.area: float = self.width * self.height
        return self.area

    def __add__(self, other: 'Rectangle') -> 'Rectangle':

        """
        Метод позволяет складывать два прямоугольника путем сложения их периметров
        и создания нового прямоугольника с соответствующими значениями ширины и высоты.
        """

        perimeter: float = self.calc_perimeter() + other.calc_perimeter()
        width: float = self.width + other.width
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other: 'Rectangle') -> 'Rectangle':

        """
        Метод позволяет вычитать один прямоугольник из другого путем вычитания их периметров
        и создания нового прямоугольника с соответствующими значениями ширины и высоты.
        """

        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self

        width: float = abs(self.width - other.width)
        perimeter: float = self.calc_perimeter() - other.calc_perimeter()
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self) -> str:

        """
        Метод возвращает строковое представление прямоугольника, включающее его периметр, ширину и высоту.
        """

        return f'Периметр = {self.calc_perimeter()}\nДлина = {self.width}\nВысота = {self.height}'


if __name__ == '__main__':
    first_rectangle: Rectangle = Rectangle(10, 20)
    second_rectangle: Rectangle = Rectangle(5)
    print(f'Первый прямоугольник:\n{first_rectangle + second_rectangle}')
    print(f'\nВторой прямоугольник:\n{first_rectangle - second_rectangle}')

    help(Rectangle)
