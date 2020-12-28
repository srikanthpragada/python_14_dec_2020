data = ("20,Guthrie", "30,Jack", "10,Joe", "20,Malcolm", "10,Marshall", "20,Roberts",
        "30,Desmond", "30,Jeff")

departments = {}
for entry in data:
    parts = entry.split(",")
    deptid = parts[0]
    empname = parts[1]
    if deptid in departments:  # Department is present then add name
        departments[deptid].append(empname)
    else:  # New dept so add dept as key and name as entry in list
        departments[deptid] = [empname]

for deptid, employees in sorted(departments.items()):
    print(f"{deptid:5}  {','.join(employees)}")
