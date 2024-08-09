import sqlite3

connection = sqlite3.connect('student_expense.db')

cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(30) NOT NULL UNIQUE,
        password VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        gender VARCHAR(30) NOT NULL,
        year VARCHAR(50) NOT NULL,
        major VARCHAR(100) NOT NULL
    )
    '''
)

connection.commit()
connection.close()