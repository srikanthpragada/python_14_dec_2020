import sqlite3

con = sqlite3.connect(r"c:\classroom\dec14\hr.db")
cur = con.cursor()
f = open('salaries.txt', 'rt')

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) != 2:
        continue  # ignore line and continue with next line

    try:
        id, salary = parts
        cur.execute("update employees set salary = ? where id = ?",
                    (salary, id))
        if cur.rowcount == 1:
            print(f"Updated Employee {id} Successfully!")
        else:
            print(f"Employee {id} not found!")
    except Exception as ex:
        print(f"Error while updating employee {id} -> {ex}")


con.commit()
f.close()
cur.close()
con.close()
