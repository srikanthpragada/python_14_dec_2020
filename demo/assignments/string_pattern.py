
s = "AB123433434Y"

middle = s[2:-2]  # Take everything except first two and last two chars
if s[:2].isalnum() and s[-2:].isalpha() and middle.isdigit():
    print("Valid Code")
else:
    print("Invalid Code")