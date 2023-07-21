from my_package.ex7_seminar import valid_date

def main() -> None:
    date_input: str = input("Введите дату в формате дд.мм.гггг: ")
    print(valid_date(date_input))
    

if __name__ == '__main__':
    main()
        