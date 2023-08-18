from student import Student

# Пример использования
student = Student("Иванов", "Иван", "Иванович", "subjects.csv")
student.add_score("Math", 4, 85)
student.add_score("Physics", 5, 92)
student.add_score("Math", 3, 78)

print("ФИО студента:", student.last_name, student.first_name, student.middle_name)
print("Предметы:", student.subjects)
print("Math - Средний балл за тесты:", student.average_test_score("Math"))
print("Physics - Средний балл за тесты:", student.average_test_score("Physics"))
print("Общий средний балл:", student.overall_average_grade())
