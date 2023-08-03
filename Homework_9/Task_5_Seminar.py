from Homework_9.my_package import guess_number_ex5

SECRET_NUMBER: int = 25
NUMBER_OF_TRIES: int = 3


def main() -> None:
    game = guess_number_ex5(SECRET_NUMBER, NUMBER_OF_TRIES)
    print(game)


if __name__ == '__main__':
    main()
