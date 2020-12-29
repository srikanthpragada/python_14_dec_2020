def print_line(length=10, char='-'):
    for n in range(length):
        print(char, end='')


print_line()
print("\nSrikanth Technologies")
print_line(char='*')  # Keyword arguments
print()
print_line(20, '.')  # Positional
