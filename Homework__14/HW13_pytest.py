import pytest
from Homework__13.Task_1 import (StudentProfile, FullNameFormatException, OutOfRangeGradeException,
                                 OutOfRangeTestScoreException, FileNotFoundCustomException,
                                 SubjectNotFoundInFileException)


@pytest.fixture
def student():
    return StudentProfile("../Homework__13/student subject.csv")


# Проверка, что исключение FullNameFormatException вызывается при неверном ФИО
def test_invalid_fullname_format(student):
    with pytest.raises(FullNameFormatException):
        student.subjects_list = "И2ванов Иван Иванович"


# Проверка, что исключение OutOfRangeGradeException вызывается при попытке добавить недопустимую оценку
def test_out_of_range_assessment(student):
    with pytest.raises(OutOfRangeGradeException):
        student.add_grade("Физика", 6)


# Проверка, что исключение FileNotFoundCustomException вызывается, когда файл не найден
def test_file_not_found():
    with pytest.raises(FileNotFoundCustomException):
        StudentProfile("new_file.csv")


# Проверка, что исключение OutOfRangeTestScoreException вызывается при попытке добавить недопустимую значение теста
def test_out_of_range_test(student):
    with pytest.raises(OutOfRangeTestScoreException):
        student.add_test_result("Информатика", 101)


# Проверка, что исключение SubjectNotFoundInFileException при отсутствии предмета в списке!
def test_subject_not_found(student):
    with pytest.raises(SubjectNotFoundInFileException):
        student.add_grade("Английский язык", 4)


# Проверка средней оценки по заданному предмету
def test_average_grade_for_subject(student):
    student.add_grade("Физика", 5)
    student.add_grade("Физика", 3)
    student.add_grade("Физика", 5)
    assert round(student.calculate_average_grade("Физика"), 2) == 4.33


# Проверка средней оценки по всем предметам
def test_average_grade_for_all_subjects(student):
    student.add_grade("Физика", 5)
    student.add_grade("Физика", 3)
    student.add_grade("Математика", 5)
    student.add_grade("Математика", 2)
    assert round(student.calculate_average_grade_all_subjects(), 2) == 3.75


# Проверка среднего результата по тестам для заданного предмета
def test_average_test_result_for_subject(student):
    student.add_test_result("Информатика", 62)
    student.add_test_result("Информатика", 85)
    student.add_test_result("Информатика", 56)
    assert round(student.calculate_average_test_result("Информатика"), 2) == 67.67


if __name__ == '__main__':
    pytest.main(['-vv'])
