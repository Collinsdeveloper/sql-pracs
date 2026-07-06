import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    completed INTEGER
)
""")

# Insert sample data
cursor.execute(
    "INSERT INTO tasks(title, completed) VALUES (?, ?)",
    ("Learn SQLite", 0)
)

cursor.execute(
    "INSERT INTO tasks(title, completed) VALUES (?, ?)",
    ("submit assignment on time", 1)
)

cursor.execute(
    "INSERT INTO tasks(title, completed) VALUES (?, ?)",
    ("Finish labs", 0)
)

conn.commit()
conn.close()

print("Database created and sample data inserted.")