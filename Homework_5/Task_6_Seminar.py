from my_package.ex6_seminar import generate_multiplication_table
from typing import Generator

def main() -> None:
    result: Generator[int, None, None] = generate_multiplication_table()
    print(*result, sep='')
    
if __name__ == '__main__':
    main()
    