def print_line(length, char):
    for n in range(length):
        print(char, end='')


print_line(25, '*')  # Passing by positional parameters
print("\nSrikanth Technologies")
print_line(char='.', length=20)  # Keyword arguments
print_line(20, char='=')  # Positional and Keyword
