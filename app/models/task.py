import sqlite3

DATABASE = 'database/tasks.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    with open('database/schema.sql', 'r', encoding='utf-8') as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()

def get_all_tasks(status=None):
    conn = get_connection()
    if status == 'completed':
        tasks = conn.execute('SELECT * FROM tasks WHERE is_completed = 1 ORDER BY id DESC').fetchall()
    elif status == 'pending':
        tasks = conn.execute('SELECT * FROM tasks WHERE is_completed = 0 ORDER BY id DESC').fetchall()
    else:
        tasks = conn.execute('SELECT * FROM tasks ORDER BY id DESC').fetchall()
    conn.close()
    return tasks

def get_task_by_id(task_id):
    conn = get_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return task

def create_task(title, description):
    conn = get_connection()
    conn.execute(
        'INSERT INTO tasks (title, description) VALUES (?, ?)',
        (title, description)
    )
    conn.commit()
    conn.close()

def update_task(task_id, title, description):
    conn = get_connection()
    conn.execute(
        'UPDATE tasks SET title = ?, description = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?',
        (title, description, task_id)
    )
    conn.commit()
    conn.close()

def delete_task_by_id(task_id):
    conn = get_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def toggle_task_status(task_id):
    conn = get_connection()
    task = conn.execute('SELECT is_completed FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task:
        new_status = 0 if task['is_completed'] == 1 else 1
        conn.execute(
            'UPDATE tasks SET is_completed = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?',
            (new_status, task_id)
        )
        conn.commit()
    conn.close()
