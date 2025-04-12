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
