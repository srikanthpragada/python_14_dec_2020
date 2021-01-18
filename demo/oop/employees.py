from abc import ABC, abstractmethod


# Superclass
class Employee(ABC):
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def __str__(self):
        return (f"Name: {self.name}, Designation: {self.designation}")

    @abstractmethod
    def getSalary(self):
        pass


class SalariedEmployee(Employee):
    def __init__(self, name, designation, salary):
        super().__init__(name, designation)
        self.salary = salary

    def getSalary(self):
        return self.salary

    def __str__(self):
        return super().__str__() + f", Salary : {self.salary}"


# Subclass2
class Consultant(Employee):
    def __init__(self, name, designation, hours, rate):
        super().__init__(name, designation)
        self.hours = hours
        self.rate = rate

    def getSalary(self):
        return self.hours * self.rate

    def __str__(self):
        return super().__str__() + f", Salary : {self.getSalary()}"


e1 = SalariedEmployee("Tom", "Manager", 200000)
print(e1)

e2 = Consultant("Mike", "Programmer", 50, 1000)
print(e2)
