import doctest
from Homework__13.Task_1 import StudentProfile


def run_tests():
    """

    >>> student: StudentProfile = StudentProfile("../Homework__13/student subject.csv")
    >>> student.subjects_list: str = "Иванов Иван Иванович"

    >>> student.add_grade("Физика", 5)
    >>> student.add_grade("Физика", 3)
    >>> student.add_grade("Математика", 5)
    >>> student.add_grade("Математика", 2)

    >>> round(student.calculate_average_grade("Физика"), 2)
    4.0
    >>> round(student.calculate_average_grade("Математика"), 2)
    3.5
    >>> round(student.calculate_average_grade_all_subjects(), 2)
    3.75

    >>> student.add_test_result("Информатика", 63)
    >>> student.add_test_result("Информатика", 86)
    >>> round(student.calculate_average_test_result("Информатика"), 2)
    74.5
    """


if __name__ == "__main__":
    doctest.testmod(verbose=True)
