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
