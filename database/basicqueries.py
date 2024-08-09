import sqlite3

def add_user(username, password, age, gender, year, major):
    connection = sqlite3.connect('database/student_expense.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO users(username, password, age, gender, year, major) VALUES (?,?,?,?,?,?)''',(username,password,age,gender,year, major))
    connection.commit()
    connection.close()

def check_for_same_username(username):
    connection = sqlite3.connect('database/student_expense.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT id from users WHERE username=?''',(username,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_user_credentials(id):
    connection = sqlite3.connect('database/student_expense.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT username, password from users WHERE id=?''',(id,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def get_user_information(username):
    connection = sqlite3.connect('database/student_expense.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT age, gender, year, major from users WHERE username=?''',(username,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()