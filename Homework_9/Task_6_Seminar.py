from Homework_9.my_package import guess_number_ex6


SECRET_NUMBER: int = 15
NUMBER_OF_TRIES: int = 2


def main() -> None:
    game = guess_number_ex6(SECRET_NUMBER, NUMBER_OF_TRIES)
    print(game)


if __name__ == '__main__':
    main()
