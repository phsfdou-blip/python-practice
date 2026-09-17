"""
practice1.py - Technical Support Practice
Focus: Python, SQLite, VS Code Source Control + Changes, GitHub Copilot
Author: phsfdou-blip
GitHub: support-practice repo
Date: 2026-09-16
This file is 95 lines for VS Code practice.
"""

import sqlite3
from datetime import date

# 1. Connect to database (creates file if not exists)
conn = sqlite3.connect("support.db")
cursor = conn.cursor()

# 2. Create users table for practice
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    role TEXT,
    city TEXT,
    skill TEXT,
    created_date TEXT
)
""")

# 3. Clean old data for fresh practice run
cursor.execute("DELETE FROM users")
conn.commit()

# 4. Sample data - 6 months of practice style data
sample_users = [
    ("Phillip", 69, "Student", "San Francisco", "Python", str(date.today())),
    ("Alex", 28, "Support", "San Jose", "Excel", str(date.today())),
    ("Maria", 35, "Technician", "Oakland", "SQLite", str(date.today())),
    ("John", 42, "Manager", "SF", "Word", str(date.today())),
    ("Lisa", 31, "Analyst", "Daly City", "AI Tools", str(date.today())),
    ("David", 25, "Intern", "SF", "GitHub", str(date.today())),
    ("Emma", 45, "Lead", "Berkeley", "VS Code", str(date.today())),
] 

# 5. Insert data using executemany (good practice)
cursor.executemany(
    "INSERT INTO users (name, age, role, city, skill, created_date) VALUES (?, ?, ?, ?, ?, ?)",
    sample_users
)
conn.commit()

# 6. Show all users - for VS Code Run
print("--- All Users ---")
all_users = cursor.execute("SELECT id, name, age, role, skill FROM users").fetchall()
for user in all_users:
    print(user)

# 7. Practice WHERE - filter example
print("\n--- Python Skill Users ---")
python_users = cursor.execute("SELECT name, skill FROM users WHERE skill = 'Python'").fetchall()
for u in python_users:
    print(u)

# 8. Practice COUNT - total users
total_count = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]
print(f"\nTotal users: {total_count}")

# 9. Practice AVG - average age
avg_age = cursor.execute("SELECT AVG(age) FROM users").fetchone()[0]
print(f"Average age: {avg_age:.1f}")

# 10. Main Task: Count users over 30 - for Copilot practice
# This is useful for support: filtering by age group / experience
users_over_30 = cursor.execute("SELECT COUNT(*) FROM users WHERE age > 30").fetchone()[0]

# 11. List who is over 30
print("\n--- Users Over 30 ---")
over_30_list = cursor.execute("SELECT name, age, role FROM users WHERE age > 30").fetchall()
for person in over_30_list:
    print(person)

# 12. Find users whose city contains SF or San Francisco
def find_san_francisco_users():
    return cursor.execute(
        "SELECT * FROM users WHERE city LIKE ? OR city LIKE ?",
        ("%SF%", "%San Francisco%")
    ).fetchall()

# 13. Close connection - always do this
conn.close()
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice
# extra comment line to reach 95 lines for practice

# 14. Final print - Line 95 as requested
print(f"Over 30: {users_over_30}")
