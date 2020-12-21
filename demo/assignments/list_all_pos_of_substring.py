s = "How do you do"
ss = "do"

pos = -1
while True:
    pos = s.find(ss, pos + 1)
    if pos == -1: # Not found 
        break
    print(pos)
