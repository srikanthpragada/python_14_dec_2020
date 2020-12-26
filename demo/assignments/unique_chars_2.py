chars = set()
names = ['Bob', 'Joe', 'John', 'Scott', 'Joseph']
for name in names:
    chars |= set(name)

print(chars)
