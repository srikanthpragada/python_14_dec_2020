class Student:
    # Static attributes or class attributes
    courses = {'Python': 10000, 'Java': 15000, 'DS': 20000}
    gst = 12.5

    @staticmethod
    def gettotalfee(course):
        fee = Student.courses.get(course,0)
        return fee + fee * Student.gst / 100

    @staticmethod
    def getcoursecount():
        return len(Student.courses)

    # Constructor
    def __init__(self, admno, name, course="Python"):
        # Object attributes
        self.admno = admno
        self.name = name
        if course not in Student.courses:
            raise ValueError("Invalid course name!")

        self.course = course
        self.feepaid = 0

    # Method
    def info(self):
        return f"{self.admno}, {self.name}, {self.course}"

    def totalfee(self):
        return Student.gettotalfee(self.course)

    def payment(self, amount):
        self.feepaid += amount

    def due(self):
        return self.totalfee() - self.feepaid


print(Student.gettotalfee(''))  # Call static method
print(Student.getcoursecount())
s1 = Student(1, "Scott")  # Create an object
s1.payment(5000)
print(s1.due())

print(s1.info())  # call method
s2 = Student(2, "Tom", "Java")
print(s2.info())
print(s2.due())
