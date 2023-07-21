from my_package.ex7_seminar import valid_date
from sys import argv

def main() -> None:
    if len(argv) < 2:
        print("Вы не указали дату для проверки!")
    else:
        date_to_check = argv[1]
        if valid_date(date_to_check):
            print("Дата является действительной!")
        else:
            print("Дата недействительна!")


if __name__ == '__main__':
    main()
    