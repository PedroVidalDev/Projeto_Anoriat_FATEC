import sqlite3

conn = sqlite3.connect("Anoriat.db")
cursor = conn.cursor()
cursor.execute('''create table users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(20) NOT NULL
) ''')

cursor.execute('''create table products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    price REAL NOT NULL
) ''')

cursor.execute('''create table layout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(40) NOT NULL,
    code VARCHAR(40) NOT NULL
) ''')

conn.commit()
cursor.close()
conn.close