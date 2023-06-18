import sqlite3

conn = sqlite3.connect("Anoriat.db")
cursor = conn.cursor()

cursor.execute("alter table products add column qnt 'int'")

cursor.close()
conn.close()