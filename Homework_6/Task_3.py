from my_package.ex3 import calculate_successful_queen_placements
from typing import List

def main() -> None:
     successful: List[List[int]]   = calculate_successful_queen_placements()
     for queens in successful:
        print(queens)
    

if __name__ == '__main__':
    main()
