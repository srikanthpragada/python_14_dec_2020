class Student:
    # Constructor
    def __init__(self, admno, name, course="Python"):
        # Object attributes
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    # Method
    def info(self):
        return f"{self.admno}, {self.name}, {self.course}"

    def totalfee(self):
        if self.course == 'Python':
            return 10000
        else:
            return 15000

    def payment(self, amount):
        self.feepaid += amount

    def due(self):
        return self.totalfee() - self.feepaid


s1 = Student(1, "Scott")  # Create an object
s1.payment(5000)
print(s1.due())

print(s1.info())  # call method
s2 = Student(2, "Tom", "Java")
s2.course = "Python"
print(s2.info())

print(type(s1))
