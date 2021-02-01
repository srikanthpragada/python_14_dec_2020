import sqlite3

con = sqlite3.connect(r"c:\classroom\dec14\hr.db")
cur = con.cursor()
cur.execute("select count(id), sum(salary), avg(salary) from employees")
count, total, average = cur.fetchone()

print(f'No. of employees : {count:10}')
print(f'Total salary     : {total:10}')
print(f'Avg. salary      : {average:10.0f}')

cur.close()
con.close()
