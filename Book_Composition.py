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


