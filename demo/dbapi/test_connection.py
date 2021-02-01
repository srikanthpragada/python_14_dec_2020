import sqlite3

con = sqlite3.connect(r"c:\classroom\dec14\hr.db")
print(con)
con.close()