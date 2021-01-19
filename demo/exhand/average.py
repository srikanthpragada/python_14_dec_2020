total = 0
count = 0

while True:
    try:
        n = int(input("Enter number [0 to stop] :"))
        if n == 0:
            break

        total += n
        count += 1
    except ValueError:
        print("Invalid Number!")

print(f"Average : {total // count}")
