import sqlite3

def add_product(name, quantity, price, category):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price, category) VALUES (?, ?, ?, ?)",
                   (name, quantity, price, category))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get_low_stock(threshold=10):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE quantity < ?", (threshold,))
    return cursor.fetchall()
