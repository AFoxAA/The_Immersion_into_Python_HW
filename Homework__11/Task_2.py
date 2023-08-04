from typing import List, Union


class Matrix:
    def __init__(self, data: List[List[int]]) -> None:
        self.data: List[List[int]] = data

    def __str__(self) -> str:
        matrix_str = "\n".join(["[" + ", ".join(map(str, row)) + "]" for row in self.data])
        return matrix_str

    def __eq__(self, other: 'Matrix') -> bool:
        matrix_size_equal = len(self.data) == len(other.data) and all(
            len(row) == len(other.data[0]) for row in self.data)
        return matrix_size_equal

    def __gt__(self, other: 'Matrix') -> bool:
        has_more_rows = len(self.data) > len(other.data)
        return has_more_rows

    def __add__(self, other: 'Matrix') -> Union['Matrix', str]:
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            return '- Матрицы имеют разный размер!'

        result_data: List[List[int]] = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in
                                        range(len(self.data))]
        return Matrix(result_data)

    def __mul__(self, other: 'Matrix') -> Union['Matrix', str]:
        if len(self.data[0]) != len(other.data):
            return f'- Ошибка умножения матриц: количество столбцов в первой матрице должно быть равно количеству\n  ' \
                   f'строк во второй матрице. Убедитесь, что вы выполняете умножение согласно этому правилу'

        result_data: List[List[int]] = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))) for j in
             range(len(other.data[0]))] for i in range(len(self.data))]
        return Matrix(result_data)


if __name__ == "__main__":
    matrix_1: Matrix = Matrix([[1, 2], [3, 4]])
    matrix_2: Matrix = Matrix([[5, 6], [7, 8]])
    matrix_3: Matrix = Matrix([[9, 10, 11], [12, 13, 14]])
    matrix_4: Matrix = Matrix([[15, 16], [17, 18], [19, 20]])

    print(f'Матрица №1:\n{matrix_1}\n')
    print(f'Матрица №2:\n{matrix_2}')
    print('-----' * 20)

    print("Матрица №1 равна матрице №2: ", matrix_1 == matrix_2)
    print("Матрица №1 больше матрицы №2: ", matrix_1 > matrix_2)
    print("Матрица №1 не равна матрице №3: ", matrix_1 != matrix_3)
    print("Матрица №1 равна матрице №3: ", matrix_1 == matrix_3)
    print("Матрица №1 больше матрицы №4: ", matrix_1 > matrix_4)
    print("Матрица №3 меньше матрицы №4: ", matrix_3 < matrix_4)
    print('-----' * 20)

    print("Сумма матрицы №1 и матрицы №2:")
    print(matrix_1 + matrix_2)

    print("\nСумма матрицы №1 и матрицы №3:")
    print(matrix_1 + matrix_3)

    print("\nПроизведение матрицы №1 и матрицы №2:")
    print(matrix_1 * matrix_2)

    print("\nПроизведение матрицы №3 и матрицы №4:")
    print(matrix_3 * matrix_4)

    print("\nПроизведение матрицы №1 и матрицы №4:")
    print(matrix_1 * matrix_4)
    print('-----' * 20)
