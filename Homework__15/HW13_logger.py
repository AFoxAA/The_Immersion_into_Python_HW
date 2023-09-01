# Запуск программы через командную строку:
# 1. Перейти в директорию Homework__15
# 2. Помощь: python .\HW13_logger.py --help
# 3. Запустить: python .\HW13_logger.py "../Homework__15/student subject.csv" "Иванов Иван Иванович"


from HW13 import (StudentProfile, FullNameFormatException, OutOfRangeGradeException,
                  OutOfRangeTestScoreException, FileNotFoundCustomException,
                  SubjectNotFoundInFileException)
import logging
import argparse


def setup_error_logger(log_file: str) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - [%(message)s] [%(filename)s]')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="\n\033[34mАргументы для запуска: \033[0m")

    parser.add_argument("student_subject_file",
                        help="\n\033[32mНеобходимо указать путь к файлу student subject.csv  с предметами студента\033[0m")
    parser.add_argument("student_name", help="\n\033[32mНеобходимо указать полное имя студента\033[0m")
    args = parser.parse_args()

    log_filename: str = "logger_file.txt"
    logger = setup_error_logger(log_filename)

    try:
        student: StudentProfile = StudentProfile(args.student_subject_file)
        student.subjects_list = args.student_name

        student.add_grade("Физика", 3)
        student.add_grade("Физика", 4)
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
              round(student.calculate_average_test_result("Информатика"), 2))

    except (FullNameFormatException, OutOfRangeGradeException, OutOfRangeTestScoreException,
            FileNotFoundCustomException,
            SubjectNotFoundInFileException) as e:
        logger.error(e)
