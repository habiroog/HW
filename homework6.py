import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


db_file = "game.db"

create_users_table_sql = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        password TEXT NOT NULL
    )
'''

conn = create_connection(db_file)

if conn is not None:
    create_table(conn, create_users_table_sql)

    cursor = conn.cursor()

    users_data = [
        ('Биба', 42, 'qwerty'),
        ('Боба', 88, '123456'),
        ('Тормозбек', 98, 'kycok_gov'),
    ]

    cursor.executemany('INSERT INTO users (name, age, password) VALUES (?, ?, ?)', users_data)

    conn.commit()
    conn.close()
else:
    print("Ошибка: Не удалось установить соединение с базой данных.")
