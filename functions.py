import sqlite3

def login(email, password):
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor() 
    cursor.execute("select * from users where email = '{}'".format(email))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def register(name, email, password):
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("insert into users (name, email, password) values (?,?,?)",(name, email, password))
    conn.commit()
    cursor.close()
    conn.close()
    return

def product_add(name, price, qnt):
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("insert into products (name, price, qnt) values (?,?,?)",(name, price, qnt))
    conn.commit()
    cursor.close()
    conn.close()
    return

def finder(id):
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("select * from products where id = '{}'".format(id))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return product

def product_remove(id):
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("delete from products where id = '{}'".format(id))
    conn.commit()
    cursor.close()
    conn.close()

def relatorio():
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("select * from products")
    relatorio = cursor.fetchall()
    return relatorio

def actualize(id, alt):
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("select * from products where id = '{}'".format(id))
    row = cursor.fetchone()
    if row is None:
        return "\n\033[1;31mO produto selecionado não existe...\033[m"
    else:
        cursor.execute("update products set qnt = '{}' where id = '{}'".format(alt, id))
        conn.commit()
        cursor.close()
        conn.close()
        return "\n\033[1;32mValor alterado com sucesso !!!\033[m"
    
def layout(name, color):
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("update layout set (color, code) = ('{}','{}') where id = 1".format(name, color))
    conn.commit()
    cursor.close()
    conn.close()
    return

def color():
    conn = sqlite3.connect("Anoriat.db")
    cursor = conn.cursor()
    cursor.execute("select code from layout where id = 1")
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res