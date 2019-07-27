import os
import sqlite3

parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = '{}/store.db'.format(parent_folder)
conn = sqlite3.connect(DATABASE)

c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS
        customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email text UNIQUE,
            address text,
            phone_number text
        )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS
        item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DOUBLE,
            photo_url TEXT,
            description TEXT
        )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS
        customer_item_order (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id INTEGER,
            customer_id INTEGER,
            FOREIGN KEY(customer_id) REFERENCES customer(id),
            FOREIGN KEY(item_id) REFERENCES item(id)
        )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS
        admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
''')

conn.close()
