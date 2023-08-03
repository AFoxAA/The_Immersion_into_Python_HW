from typing import List
from Homework_9.my_package import calculate_sum

FIRST_NUMBER: int = 15
SECOND_NUMBER: int = 35


def main() -> None:
    results: List[int] = calculate_sum(FIRST_NUMBER, SECOND_NUMBER)
    print(results)


if __name__ == '__main__':
    main()
