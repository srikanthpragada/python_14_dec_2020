def wish(*names, message='Hello'):
    for n in names:
        print(message, n)


wish("James", "Steve", message="Hi")
wish("Bill", "Larry", "Mike")
