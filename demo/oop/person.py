class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


p = Person("Rossum", 54)
print(p.__dict__)
print(p._Person__age)
