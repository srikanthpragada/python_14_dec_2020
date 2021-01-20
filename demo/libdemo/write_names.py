# Write names into names.txt

f = open("names.txt", "wt")  # Write Text

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break
    f.write(name + "\n")

f.close()