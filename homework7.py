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


def insert_student(conn, student):
    sql = "INSERT INTO students(hobby, first_name, last_name, birth_year, homework_score) VALUES(?,?,?,?,?)"
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()
    return cursor.lastrowid


def fetch_students_with_long_last_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE LENGTH(last_name) > 10")
    return cursor.fetchall()


def update_students_score_above_10(conn):
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET first_name = 'genius' WHERE homework_score > 10")
    conn.commit()


def fetch_genius_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE first_name = 'genius'")
    return cursor.fetchall()


def delete_even_id_students(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id % 2 = 0")
    conn.commit()


db_file = "students.db"

create_students_table_sql = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hobby TEXT,
        first_name TEXT,
        last_name TEXT,
        birth_year INTEGER,
        homework_score INTEGER
    )
'''

conn = create_connection(db_file)

if conn is not None:
    create_table(conn, create_students_table_sql)

    students_data = [
        ('Читать', 'Лакшери', 'Герл', 2000, 15),
        ('Играть', 'Биба', 'Хабиба', 1998, 8),
        ('Поплавок', 'Боба', 'Джонисон', 1997, 12),
        ('Гадить', 'Бил', 'Редлипс', 1999, 5),
        ('Музикль', 'Ева', 'Эльфи', 1996, 18),
        ('ТикиТак', 'Индиана', 'Джонс', 1994, 7),
        ('Пэйнтинг', 'Хабиб', 'Нургамамбетов', 2000, 14),
        ('Кукинг', 'Саша', 'Десятьбукв', 1998, 9),
        ('Дэнсинг', 'Улугбек', 'Турбопушка', 1997, 20),
        ('Пукинг', 'Анджелина', 'Жёли', 1999, 3),
    ]

    for student_data in students_data:
        insert_student(conn, student_data)

    students_with_long_last_names = fetch_students_with_long_last_names(conn)
    print("Students with long last names:")
    for student in students_with_long_last_names:
        print(student)

    update_students_score_above_10(conn)
    genius_students = fetch_genius_students(conn)
    print("\nGenius students:")
    for student in genius_students:
        print(student)

    delete_even_id_students(conn)
    print("\nDeleted students with even IDs.")

    conn.close()
else:
    print("Ошибка: Не удалось установить соединение с базой данных.")
