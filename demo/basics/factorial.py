num = int(input("Enter a number :"))

fact = 1
for n in range(2, num + 1):
    fact = fact * n

print(f"Factorial of {num} is {fact}")