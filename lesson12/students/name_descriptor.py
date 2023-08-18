class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError("Name should contain only letters.")
        if not value.istitle():
            raise ValueError("Name should start with a capital letter.")
        instance._name = value


class Student:
    last_name = NameDescriptor()
    first_name = NameDescriptor()
    middle_name = NameDescriptor()

    def __init__(self, last_name, first_name, middle_name, subjects_file):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.subjects = self.load_subjects(subjects_file)
        self.scores = {subject: {"grades": [], "test_results": []} for subject in self.subjects}

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = [row[0] for row in reader]
        return subjects

    def add_score(self, subject, grade, test_result):
        if subject not in self.subjects:
            raise ValueError(f"{subject} is not a valid subject.")
        if grade < 2 or grade > 5:
            raise ValueError("Grade should be between 2 and 5.")
        if test_result < 0 or test_result > 100:
            raise ValueError("Test result should be between 0 and 100.")
        self.scores[subject]["grades"].append(grade)
        self.scores[subject]["test_results"].append(test_result)

    def average_test_score(self, subject):
        test_results = self.scores[subject]["test_results"]
        if not test_results:
            return 0
        return sum(test_results) / len(test_results)

    def overall_average_grade(self):
        total_grades = []
        for subject_scores in self.scores.values():
            total_grades.extend(subject_scores["grades"])
        if not total_grades:
            return 0
        return sum(total_grades) / len(total_grades)
