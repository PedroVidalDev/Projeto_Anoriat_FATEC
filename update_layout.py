import sqlite3

conn = sqlite3.connect("Anoriat.db")
cursor = conn.cursor()

nome = "Cyan"
code = "\033[1;37;46m"

cursor.execute("insert into layout(color, code) values (?,?)",(nome, code))
conn.commit()
cursor.close()
conn.close()