import sqlite3
conn = sqlite3.connect('myjobs.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM applications")
print(cursor.fetchall())

