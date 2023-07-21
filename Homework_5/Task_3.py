from my_package.ex3 import fibonacci_numbers_generator
from typing import Generator

def main() -> None:
    result_of_fibonacci_numbers: Generator[int, None, None] = fibonacci_numbers_generator()
    for _ in range(10):
        print(next(result_of_fibonacci_numbers), end=' ')
    

if __name__ == '__main__':
    main()
    