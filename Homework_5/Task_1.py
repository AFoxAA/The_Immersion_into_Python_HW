from my_package.ex1 import split_absolute_path
from typing import Tuple

def main() -> None:
    path: str = "/Homework/Homework_5/Семинар_5: Погружение в Python.Итераторы и генераторы.pdf"
    result: Tuple[str, str, str] = split_absolute_path(path)
    print(result)
    
if __name__ == '__main__':
    main()
    