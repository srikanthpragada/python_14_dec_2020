def prepend(lst, value):
    lst.insert(0, value)


def zero(n):
    print(id(n))
    n = 0


a = 100
lst = [1, 2]
print(id(a))
zero(a)
print(a)

prepend(lst, 10)
print(lst)
