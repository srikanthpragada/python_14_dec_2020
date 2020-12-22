
s = "how do you do"

used_chars = []
for ch in s:
    if ch not in used_chars:
        print(f"{ch} - {s.count(ch)}")
        used_chars.append(ch)