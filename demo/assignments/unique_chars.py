chars = set()
while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    chars |= set(name)

print(chars)
