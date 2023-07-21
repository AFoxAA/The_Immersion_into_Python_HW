from my_package.ex2 import bonus_сalculation
from typing import Dict, List

def main() -> None:
    result: Dict[str, float] = bonus_сalculation(names, rates, bonus_percentage)
    print(result)
        
        
if __name__ == '__main__':
    names: List[str] = ["Name_1", "Name_2", "Name_3"]
    rates: List[str] = [930, 680, 1410]
    bonus_percentage: List[str] = ["6.55%", "4.25%", "5.70%"]
    main()
