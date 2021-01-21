f = open("marks.txt", "rt")

for line in f.readlines():
    total = count = 0
    for v in line.split(","):
        try:
            m = int(v)
            total += m
            count += 1
        except:
            pass

    print(f"{total:4}  {total // count:3}")

f.close()
