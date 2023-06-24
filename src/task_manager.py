import sqlite3

class Task:
    def __init__(self, id, name, due_date=None, priority=None, category=None, completed=False):
        self.id = id
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                due_date TEXT,
                priority INTEGER,
                category TEXT,
                completed INTEGER DEFAULT 0
            )
        ''')

        self.conn.commit()

    def add_task(self, name, due_date=None, priority=None, category=None):
        if not name:
            return 'Error: Task name cannot be empty.'
        
        self.cursor.execute('SELECT * FROM tasks WHERE name = ?', (name,))
        if self.cursor.fetchone() is not None:
            return f'Error: Task "{name}" already exists.'

        try:
            self.cursor.execute('''
                INSERT INTO tasks (name, due_date, priority, category) 
                VALUES (?, ?, ?, ?)
            ''', (name, due_date, priority, category))

            self.conn.commit()
        except sqlite3.Error as e:
            return f'Error: Could not add task. {e}'

    def complete_task(self, name):
        self.cursor.execute('SELECT * FROM tasks WHERE name = ?', (name,))
        task = self.cursor.fetchone()
        if task is None:
            return f'Error: Task "{name}" does not exist.'
        elif task[-1] == 1:
            return f'Error: Task "{name}" is already completed.'

        try:
            self.cursor.execute('''
                UPDATE tasks SET completed = 1 WHERE name = ?
            ''', (name,))

            self.conn.commit()
        except sqlite3.Error as e:
            return f'Error: Could not complete task. {e}'

    def get_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        return [Task(*row) for row in self.cursor.fetchall()]
