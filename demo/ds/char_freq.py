s = "how do you do"

for ch in sorted(set(s)):
    print(f"{ch} - {s.count(ch)}")
