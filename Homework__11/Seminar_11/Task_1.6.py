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

    def __add__(self, other) -> "Rectangle":
        """
        Метод позволяет складывать два прямоугольника путем сложения их периметров
        и создания нового прямоугольника с соответствующими значениями ширины и высоты.
        """
        perimeter: float = self.calc_perimeter() + other.calc_perimeter()
        width: float = self.width + other.width
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other) -> "Rectangle":
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
        return f'\nПериметр = {self.calc_perimeter()}\nДлина = {self.width}\nВысота = {self.height}\n'

    def __eq__(self, other: object) -> bool:
        """
        Метод позволяет сравнивать прямоугольники по площади на равенство (==).
        """
        return self.calc_area() == other.calc_area()

    def __lt__(self, other: object) -> bool:
        """
        Метод позволяет сравнивать прямоугольники по площади на "меньше" (<).
        """
        return self.calc_area() < other.calc_area()

    def __le__(self, other: object) -> bool:
        """
        Метод позволяет сравнивать прямоугольники по площади на "меньше или равно" (<=).
        """
        return self.calc_area() <= other.calc_area()

    def print_info(self):
        """
        Метод выводит информацию о прямоугольнике, используя метод __str__, который уже определен в классе.
        Выводит строковое представление прямоугольника, включающее его периметр, ширину и высоту.
        """
        print(self)


if __name__ == '__main__':
    first_rectangle: Rectangle = Rectangle(5, 30)
    second_rectangle: Rectangle = Rectangle(30, 5)

    first_rectangle.print_info()
    second_rectangle.print_info()

    print("Площади равны:", first_rectangle == second_rectangle)
    print("Площадь нового прямоугольника меньше:", first_rectangle < second_rectangle)
    print("Площадь нового прямоугольника меньше или равна:", first_rectangle <= second_rectangle)

    help(Rectangle)
