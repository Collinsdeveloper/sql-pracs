import sqlite3


# Get all tasks
def get_all_tasks():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")

        return cursor.fetchall()


# Get one task by ID
def get_task_by_id(task_id):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        )

        return cursor.fetchone()


# Get incomplete tasks ordered by ID (newest first)
def get_incomplete_tasks():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE completed = 0
            ORDER BY id DESC
        """)

        return cursor.fetchall()


# ------------------------
# Main Program
# ------------------------

print("ALL TASKS")
print("----------------")

tasks = get_all_tasks()

for task in tasks:
    print(task)

print("\nTASK WITH ID = 1")
print("----------------")

task = get_task_by_id(1)
print(task)

print("\nINCOMPLETE TASKS")
print("----------------")

tasks = get_incomplete_tasks()

for task in tasks:
    print(task)