from my_package.ex2 import queens_no_collisions
from typing import List, Tuple

def main() -> None:
    queens_arrangement: List[Tuple[int, int]] = [(1, 1), (2, 7), (3, 5), (4, 8), (5, 2), (6, 4), (7, 6), (8, 3)] # True
    # queens_arrangement: List[Tuple[int, int]] = [(1, 1), (2, 6), (3, 4), (4, 7), (5, 3), (6, 2), (7, 8), (8, 5)] # False
    print(queens_no_collisions(queens_arrangement))
    

if __name__ == '__main__':
    main()