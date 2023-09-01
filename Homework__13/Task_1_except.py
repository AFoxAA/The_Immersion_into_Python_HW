class FullNameFormatException(Exception):
    def __str__(self):
        return '\n\033[31m"ФИО должно начинаться с заглавной буквы и содержать только буквы!"\033[0m'


class OutOfRangeGradeException(Exception):
    def __str__(self):
        return '\n\033[31m"Оценка должна находиться в диапазоне от 2 до 5!"\033[0m'


class OutOfRangeTestScoreException(Exception):
    def __str__(self):
        return '\n\033[31m"Тест должен находиться в диапазоне от 0 до 100!"\033[0m'


class FileNotFoundCustomException(Exception):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"\n\033[31mФайл '{self.file_name}' не найден!\033[0m"


class SubjectNotFoundInFileException(Exception):
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __str__(self):
        return f"\n\033[31mПредмет '{self.subject_name}' отсутствует в списке!\033[0m"



