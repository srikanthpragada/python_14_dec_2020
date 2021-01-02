# Sort strings by ignoring digits
def exclude_digits(n):
    s = ''
    for c in n:
        if not c.isdigit():
            s += c

    return s


names = ['Abc123', '123Abc', '23Xy', 'Pqr', '34Bc']

for n in sorted(names, key=exclude_digits):
    print(n)
