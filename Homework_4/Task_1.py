# Функция для транспонирования матрицы
def transposed_matrix(matrix: list[list[int]]) -> list[list[int]]:
    rows: int = len(matrix)
    columns: int = len(matrix[0])

    transposed: list[list[int]] = [[matrix[i][j] for i in range(rows)] for j in range(columns)]

    return transposed

def __main() -> None:
    # Исходная матрица
    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print('\n\033[93m\033[4mНачальная матрица:\n\033[0m')
    for row in matrix:
        print(row)

    modified_matrix: list[list[int]] = transposed_matrix(matrix)

    print('\n\033[93m\033[4mТранспонированная матрица:\n\033[0m')
    for row in modified_matrix:
        print(row)
        
if __name__ == '__main__':
    __main()