import sqlite3

DB_NAME = 'database.db'


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_user(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False


def check_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM users WHERE username=? AND password=?',
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    return user is not None
