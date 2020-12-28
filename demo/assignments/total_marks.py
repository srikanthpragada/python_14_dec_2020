data = ("Mike,50,70,80", "Bill,90,78,77,66", "Scott,67,87,77",
        "Richards,98,88,76,87")

students = {}
for entry in data:
    parts = entry.split(",")
    name = parts[0]
    # Take marks from index 1 and convert all of them to int
    marks = [int(m) for m in parts[1:]]
    students[parts[0]] = marks

for name,marks in sorted(students.items()):
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name:10} {total:3}  {avg:5.2f}")
