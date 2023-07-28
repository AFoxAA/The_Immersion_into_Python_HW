from Homework_7.my_package import generate_files_with_extensions, sort_files_by_extension

FILES_OF_THE_FILE_GROUP = 20
FILE_WITH_NEW_EXTENSION = 3


def main() -> None:
    additional_directory: str = 'Файлы, которые не подошли для сортировки'
    final_directory: str = 'Сортировка файлов по директориям'
    unincluded_files: list[str] = ['.xlsx', '.xap', '.jpeg']
    necessary_directories: dict[str, list[str]] = {'Видео': ['.mp4', '.avi', '.mov'],
                                                   'Изображения': ['.jpg', '.png', '.gif'],
                                                   'Текст': ['.txt', '.doc', '.pdf']}

    file_extensions: list[str] = []
    for extensions in necessary_directories.values():
        file_extensions.extend(extensions)

    generate_files_with_extensions(additional_directory, file_extensions, FILES_OF_THE_FILE_GROUP)
    generate_files_with_extensions(additional_directory, unincluded_files, FILE_WITH_NEW_EXTENSION)
    sort_files_by_extension(necessary_directories, additional_directory, final_directory)


if __name__ == '__main__':
    main()
