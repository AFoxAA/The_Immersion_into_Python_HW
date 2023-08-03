from Homework_9.my_package import generate_random_numbers_csv, calculate_quadratic_roots


def main() -> None:
    try:
        filename: str = 'Task_1.csv'
        generate_random_numbers_csv(filename)
        calculate_quadratic_roots(filename)

        print('\nНахождение корней квадратного уравнения выполнено успешно!')
    except Exception:
        print('\nОшибка при нахождении корней квадратного уравнения!')


if __name__ == '__main__':
    main()
