from Homework_7.my_package import create_random_file, create_multiple_files


def __main():
    directory: str = 'Task_6'
    extensions: list[str] = ['pdf', 'txt', 'jpg']
    num_files: list[int] = [5, 10, 3]

    create_random_file(directory, extensions)
    create_multiple_files(directory, extensions, num_files)


if __name__ == '__main__':
    __main()
