from typing import List, Any, Iterable
import csv
import os
from Task_1_except import FullNameFormatException, OutOfRangeGradeException, OutOfRangeTestScoreException, \
    FileNotFoundCustomException, SubjectNotFoundInFileException


class FormattedNameDescriptor:
    def __set_name__(self, owner: Any, name: str) -> None:
        self.assigned_attribute: str = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        return instance.__dict__[self.assigned_attribute]

    def __set__(self, instance: Any, value: str) -> Any:
        formatted_name: str = value.replace(" ", "")

        if formatted_name and formatted_name.isalpha() and value.istitle():
            instance.__dict__[self.assigned_attribute] = value
        else:
            raise FullNameFormatException()


class StudentSubject:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.grade_scores: List[int] = []
        self.test_scores: List[int] = []

    def add_grade_score(self, scores: int) -> None:
        if 2 <= scores <= 5:
            self.grade_scores.append(scores)
        else:
            raise OutOfRangeGradeException()

    def add_test_score(self, result: int) -> None:
        if 0 <= result <= 100:
            self.test_scores.append(result)
        else:
            raise OutOfRangeTestScoreException()


class StudentProfile:
    subjects_list: FormattedNameDescriptor = FormattedNameDescriptor()

    def __init__(self, csv_file: str) -> None:
        if not os.path.exists(csv_file):
            raise FileNotFoundCustomException(csv_file)

        self.student_subjects: List[StudentSubject] = self.load_subjects_from_csv(csv_file)

    def load_subjects_from_csv(self, csv_file: str) -> List[StudentSubject]:
        student_subjects: List[StudentSubject] = []

        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader: Iterable = csv.reader(file)

            for row in reader:
                subject_title: str = row[0]
                student_subjects.append(StudentSubject(subject_title))

        return student_subjects

    def get_subject(self, subject_name: str) -> StudentSubject:
        for student_subject in self.student_subjects:
            if student_subject.name == subject_name:
                return student_subject

        raise SubjectNotFoundInFileException(subject_name)

    def add_grade(self, subject_name: str, grade: int) -> None:
        student_subject: StudentSubject = self.get_subject(subject_name)
        student_subject.add_grade_score(grade)

    def add_test_result(self, subject_name: str, result: int) -> None:
        student_subject: StudentSubject = self.get_subject(subject_name)
        student_subject.add_test_score(result)

    def calculate_average_grade(self, subject_name: str) -> float:
        student_subject: StudentSubject = self.get_subject(subject_name)

        if student_subject.grade_scores:
            return sum(student_subject.grade_scores) / len(student_subject.grade_scores)

        return 0.0

    def calculate_average_grade_all_subjects(self) -> float:
        student_grades: List[int] = [grade for subject in self.student_subjects for grade in subject.grade_scores]

        if student_grades:
            return sum(student_grades) / len(student_grades)

        return 0.0

    def calculate_average_test_result(self, subject_name: str) -> float:
        student_subject: StudentSubject = self.get_subject(subject_name)

        if student_subject.test_scores:
            return sum(student_subject.test_scores) / len(student_subject.test_scores)

        return 0.0


if __name__ == "__main__":
    try:
        student: StudentProfile = StudentProfile("student subject.csv")
        student.subjects_list: str = "Иванов Иван Иванович"

        student.add_grade("Физика", 5)
        student.add_grade("Физика", 3)
        student.add_grade("Математика", 5)
        student.add_grade("Математика", 2)

        print("\nДневник:\n\033[32mСредний балл по Физике: \033[0m",
              round(student.calculate_average_grade("Физика"), 2))
        print("\033[32mСредний балл по Математике: \033[0m", round(student.calculate_average_grade("Математика"), 2))
        print("\033[32mОбщий средний балл по всем предметам: \033[0m",
              round(student.calculate_average_grade_all_subjects(), 2))

        student.add_test_result("Информатика", 63)
        student.add_test_result("Информатика", 86)
        print("\033[32mСредний результат тестов по Информатике: \033[0m",
              round(student.calculate_average_test_result("Инфрматика"), 2))

    except (
    FullNameFormatException, OutOfRangeGradeException, OutOfRangeTestScoreException, FileNotFoundCustomException,
    SubjectNotFoundInFileException) as e:
        print(f"\n\033[31mОшибка: {e}\033[0m")
