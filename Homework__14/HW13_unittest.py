import unittest
from Homework__13.Task_1 import (StudentProfile, FullNameFormatException, OutOfRangeGradeException,
                                 OutOfRangeTestScoreException, FileNotFoundCustomException,
                                 SubjectNotFoundInFileException)


class TestStudentProfile(unittest.TestCase):

    # Инициализация профиля студента
    def initialize_student_profile(self):
        self.student: StudentProfile = StudentProfile("../Homework__13/student subject.csv")

    # Проверка, что исключение FullNameFormatException вызывается при неверном ФИО
    def test_invalid_fullname_format(self):
        with self.assertRaises(FullNameFormatException):
            self.initialize_student_profile()
            self.student.subjects_list = "Иванов иван Иванович"

    # Проверка, что исключение OutOfRangeGradeException вызывается при попытке добавить недопустимую оценку
    def test_out_of_range_assessment(self):
        self.initialize_student_profile()
        with self.assertRaises(OutOfRangeGradeException):
            self.student.add_grade("Физика", 1)

    # Проверка, что исключение FileNotFoundCustomException вызывается, когда файл не найден
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundCustomException):
            StudentProfile("new_file.csv")

    # Проверка, что исключение OutOfRangeTestScoreException вызывается при попытке добавить недопустимую значение теста
    def test_out_of_range_test(self):
        self.initialize_student_profile()
        with self.assertRaises(OutOfRangeTestScoreException):
            self.student.add_test_result("Информатика", 101)

    # Проверка, что исключение SubjectNotFoundInFileException при отсутствии предмета в списке!
    def test_subject_not_found(self):
        self.initialize_student_profile()
        with self.assertRaises(SubjectNotFoundInFileException):
            self.student.add_grade("Английский язык", 4)

    # Проверка средней оценки по заданному предмету
    def test_get_average_grade(self):
        self.initialize_student_profile()
        self.student.add_grade("Физика", 5)
        self.student.add_grade("Физика", 3)
        self.student.add_grade("Физика", 5)
        self.assertEqual(round(self.student.calculate_average_grade("Физика"), 2), 4.33)

    # Проверка средней оценки по всем предметам
    def test_average_grade_for_all_subjects(self):
        self.initialize_student_profile()
        self.student.add_grade("Физика", 5)
        self.student.add_grade("Физика", 3)
        self.student.add_grade("Математика", 5)
        self.student.add_grade("Математика", 2)
        self.assertEqual(round(self.student.calculate_average_grade_all_subjects(), 2), 3.75)

    # Проверка среднего результата по тестам для заданного предмета
    def test_average_test_result_for_subject(self):
        self.initialize_student_profile()
        self.student.add_test_result("Информатика", 62)
        self.student.add_test_result("Информатика", 85)
        self.student.add_test_result("Информатика", 56)
        self.assertEqual(round(self.student.calculate_average_test_result("Информатика"), 2), 67.67)


if __name__ == "__main__":
    unittest.main(verbosity=2)
