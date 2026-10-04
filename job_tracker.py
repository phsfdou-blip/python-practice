import sqlite3
from datetime import date

conn = sqlite3.connect('myjobs.db')
cursor = conn.cursor()

# 1. Add status if not exists (safe to run twice)
try:
    cursor.execute("ALTER TABLE applications ADD COLUMN status TEXT")
except:
    pass

# 2. UPDATE - change Meta to Applied today
today = str(date.today())
cursor.execute("UPDATE applications SET status = ?, date_applied = ? WHERE company = ?", 
               ("Applied", today, "Meta"))

# 3. INSERT - add your 4th Bay Area company
cursor.execute("INSERT INTO applications (company, job_title, date_applied, status) VALUES (?, ?, ?, ?)",
               ("Apple", "Tech Support", today, "Learning"))

conn.commit()

# 4. SEARCH - show only Applied jobs
print("=== All Jobs ===")
for row in cursor.execute("SELECT company, job_title, status FROM applications"):
    print(row)

print("\n=== Only Applied ===")
for row in cursor.execute("SELECT company FROM applications WHERE status = 'Applied'"):
    print(row)

conn.close()