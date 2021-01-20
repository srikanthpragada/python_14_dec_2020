f = open("marks.txt", "rt")

for line in f.readlines():
    # marks =[int(m) for m in line.split(",")]
    marks = map(int, line.split(","))
    print(sum(marks))


f.close()
