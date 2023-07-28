from Homework_7.my_package import generate_random_filename, generate_multiple_files


def main() -> None:
    extensions: list[str] = ['pdf', 'txt', 'jpg']
    num_files: list[int] = [7, 5, 3]

    generate_random_filename(extensions)
    generate_multiple_files(extensions, num_files)


if __name__ == '__main__':
    main()
