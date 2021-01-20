# Read names from names.txt

f = open("names.txt", "rt")  # Write Text

for line in sorted(f):
    print(line.strip())

f.close()