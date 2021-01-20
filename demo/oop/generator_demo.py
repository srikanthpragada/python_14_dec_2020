def numbers():
    for n in range(1, 10):
        yield n


# Generator that returns only uppercase letters from a given string
def upper(s):
    for c in s:
        if c.isupper():
            yield c


g = numbers()
print(type(g))
# for v in g:
#     print(v)

# print(next(g))
# print(next(g))

for c in upper("How Do you DO"):
    print(c)