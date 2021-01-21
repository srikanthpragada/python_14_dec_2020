# Remove blank lines from names.txt

FILENAME = "names.txt"

f = open(FILENAME, "rt")
lines = []
for line in f.readlines():
    if len(line.strip()) != 0:  # non-blank line
        lines.append(line.strip())

f.close()

# Write lines to file
f = open(FILENAME, "wt")
for line in sorted(lines):
    f.write(line + "\n")

f.close()

