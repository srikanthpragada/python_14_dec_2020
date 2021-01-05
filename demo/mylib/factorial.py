import sys

if len(sys.argv) < 2:
    print("Usage : python factorial.py <number>")
    exit(0)

for v in sys.argv[1:]:
    num = int(v)
    fact = 1
    for n in range(2, num + 1):
        fact = fact * n

    print(f"Factorial of {num} is {fact}")
