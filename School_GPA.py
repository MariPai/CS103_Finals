from abc import ABC, abstractmethod

# Abstract base class
class SchoolBase(ABC):
    @abstractmethod
    def display_student_averages(self):
        pass

    @abstractmethod
    def calculate_gpa(self):
        pass

# Shared student structure
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} - Grades: {self.grades}"

# SchoolOne implementation
class SchoolOne(SchoolBase):
    def __init__(self, students):
        self.students = students

    def display_student_averages(self):
        print("=== SchoolOne Student Averages ===")
        for student in self.students:
            avg = student.average()
            print(f"{student.name}'s Average Grade: {avg:.1f}")
        print()

    def calculate_gpa(self):
        total = sum(student.average() for student in self.students)
        gpa = total / len(self.students)
        print(f"SchoolOne GPA: {gpa:.1f}")
        print()

# SchoolTwo implementation
class SchoolTwo(SchoolBase):
    def __init__(self, students):
        self.students = students

    def display_student_averages(self):
        print("=== SchoolTwo Student Averages ===")
        for student in self.students:
            avg = student.average()
            print(f"{student.name}'s Average Grade: {avg:.1f}")
        print()

    def calculate_gpa(self):
        total = sum(student.average() for student in self.students)
        gpa = total / len(self.students)
        print(f"SchoolTwo GPA: {gpa:.1f}")
        print()

# Invalid Example (not a school)
class TutoringCenter:
    def __init__(self, tutor_name):
        self.tutor_name = tutor_name

    def __str__(self):
        return f"Tutoring Center by {self.tutor_name}"

# Test block
if __name__ == "__main__":
    students_one = [
        Student("Anella Louise", [90, 92, 96]),
        Student("Marvin Teodocio", [85, 87, 90])
    ]

    students_two = [
        Student("Maria Decena", [88, 91, 93]),
        Student("John Prats", [76, 80, 79])
    ]

    school1 = SchoolOne(students_one)
    school2 = SchoolTwo(students_two)
    not_a_school = TutoringCenter("Mr. Lee")

    schools = [school1, school2, not_a_school]

    for school in schools:
        print(f"Object: {school}")
        if isinstance(school, SchoolBase):
            school.display_student_averages()
            school.calculate_gpa()
        else:
            print("→ This is NOT a School instance.")
            print()
