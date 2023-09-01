class FullNameFormatException(Exception):
    def __str__(self):
        return 'ФИО должно начинаться с заглавной буквы и содержать только буквы!'


class OutOfRangeGradeException(Exception):
    def __str__(self):
        return 'Оценка должна находиться в диапазоне от 2 до 5!'


class OutOfRangeTestScoreException(Exception):
    def __str__(self):
        return 'Тест должен находиться в диапазоне от 0 до 100!'


class FileNotFoundCustomException(Exception):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f'Файл "{self.file_name}" не найден!'


class SubjectNotFoundInFileException(Exception):
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __str__(self):
        return f'Предмет {self.subject_name} отсутствует в списке!'
