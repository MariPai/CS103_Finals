Main.py 

#1 Bus= Vehicle 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    @abstractmethod
    def start_engine(self):
        pass

    def __str__(self):
        return f"{self._brand} {self._model}"

class SchoolBus(Vehicle):
    def start_engine(self):
        return f"{self} Bus engine started."

class SUV(Vehicle):
    def start_engine(self):
        return f"{self} SUV engine started."

class Sedan(Vehicle):
    def start_engine(self):
        return f"{self} Sedan engine started."

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self} Motorcycle engine revs up."

class Skateboard:
    def __init__(self, brand, style):
        self.brand = brand
        self.style = style

    def ride(self):
        return f"Riding a {self.brand} {self.style} skateboard!"

# Testing
vehicles = [
    SchoolBus("Ford", "Transit"),
    SUV("Nissan", "Terra"),
    Sedan("Toyota", "Camry"),
    Motorcycle("Yamaha", "PG-1"),
    Skateboard("Tony Hawk", "Full Skull")
]

for v in vehicles:
    print(f"Object: {v}")
    if isinstance(v, Vehicle):
        print("→ This is a Vehicle.")
        print(v.start_engine())
    else:
        print("→ This is NOT a Vehicle.")
        print(v.ride())
    print()

#2 Employees+ Constructors 
from abc import ABC, abstractmethod

# Abstract base class
class BasePerson(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Employee class with multiple constructors
class Employee(BasePerson):
    def __init__(self, name, position, salary):
        self._name = name
        self._position = position
        self._salary = salary

    @classmethod
    def from_string(cls, emp_string):
        name, position, salary = emp_string.split(",")
        return cls(name.strip(), position.strip(), float(salary.strip()))

    @classmethod
    def create_intern(cls, name):
        return cls(name, "Intern", 0.0)

    @classmethod
    def create_contractor(cls, name, hourly_rate):
        return cls(name, "Contractor", hourly_rate * 160)

    def get_details(self):
        return f"{self._name} - {self._position} - Php{self._salary:.2f}"

    def __str__(self):
        return self.get_details()

#  Invalid non-employee example
class Freelancer:
    def __init__(self, name, project):
        self.name = name
        self.project = project

    def info(self):
        return f"{self.name} works on {self.project} as a freelancer."

    def __str__(self):
        return self.info()

# Test block
if __name__ == "__main__":
    emp1 = Employee("Alice", "Manager", 80000)
    emp2 = Employee.from_string("Fredrick, Developer, 60000")
    emp3 = Employee.create_intern("James")
    emp4 = Employee.create_contractor("Sarah", 50)
    not_employee = Freelancer("Eunice", "App UI Redesign")

    people = [emp1, emp2, emp3, emp4, not_employee]

    for person in people:
        print(f"Object: {person}")
        if isinstance(person, Employee):
            print("→ This is an Employee.")
        else:
            print("→ This is NOT an Employee.")
        print()


#3 School 1 and School 2 GPA

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


#4 Operator Overloading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Adding only Vector instances
        if not isinstance(other, Vector):
            raise TypeError("Error: Only Vector instances can be added.")
        
        # Vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Test block
if __name__ == "__main__":
    v1 = Vector(5, 12)
    v2 = Vector(13, 23)
    
    # This will successfully add v1 and v2
    try:
        sum_vector = v1 + v2
        print("Sum:", sum_vector)
    except TypeError as e:
        print(e)

    # This will raise the TypeError because we're adding a non-vector type
    try:
        invalid_add = v1 + "not a vector"
        print("Sum:", invalid_add)
    except TypeError as e:
        print(e)


#5 Book Comp

from abc import ABC, abstractmethod

class AbstractAuthor(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Author(AbstractAuthor):
    def __init__(self, name, country):
        self._name = name
        self._country = country

    def get_name(self):
        return f"{self._name} ({self._country})"

    def __str__(self):
        return self.get_name()

class Book:
    def __init__(self, title, author: AbstractAuthor):
        self._title = title
        self._author = author

    def __str__(self):
        return f"'{self._title}' by {self._author}"

# Test
a1 = Author("George Orwell", "UK")
a2 = Author("Murakami", "Japan")
a3 = Author("J.K. Rowling", "UK")

b1 = Book("1984", a1)
b2 = Book("Norwegian Wood", a2)
b3 = Book("Harry Potter", a3)

print(b1)
print(b2)
print(b3)

# Optional wrong composition
class Publisher:
    def __init__(self, name):
        self.name = name


