import sqlite3

conn = sqlite3.connect('item.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)''')

c.execute('insert into items (name, price) values (?, ?)', ('Item 1', 10.99))
c.execute('insert into items (name, price) values (?, ?)', ('Item 2', 20.99))
c.execute('insert into items (name, price) values (?, ?)', ('Item 3', 30.99))
print('Items inserted successfully.')