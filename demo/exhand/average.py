
total = 0
count = 0

while True:
    try:
        n = int(input("Enter number [0 to stop] :"))
    except ValueError:
        print("Invalid Number!")
        continue

    if n == 0:
        break

    total += n
    count += 1

print(f"Average : {total//count}")
