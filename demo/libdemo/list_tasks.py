from datetime import *

f = open("tasks.txt", "rt")
tasks = []

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    task = parts[0]
    try:
        sd = datetime.strptime(parts[1], '%Y-%m-%d')
    except:
        continue

    if len(parts) == 3:
        try:
            ed = datetime.strptime(parts[2], '%Y-%m-%d')
            status = "Completed"
            nodays = (ed - sd).days
        except:
            continue
    else:
        status = "On Going"
        nodays = (datetime.now() - sd).days

    tasks.append((task, sd, nodays, status))


for task,sd,nodays,status in sorted(tasks, key = lambda t: t[1]):
    print(f"{task:50} {sd.strftime('%d-%m-%Y'):10} {nodays:2} {status}")