import sqlite3

con = sqlite3.connect(r"c:\classroom\dec14\hr.db")
cur = con.cursor()
id = int(input("Enter id :"))
cur.execute(f"select * from employees where  id = {id}")
employee = cur.fetchone()
# fetchone() returns None if no row found otherwise it returns tuple
if employee is None:
    print("Sorry! Employee id not found!")
else:
    print(employee[1], employee[2], employee[3])
cur.close()
con.close()
