# import sqlite3

import sqlite3

# create connection
conn = sqlite3.connect("new1.db")

# create cursor
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE cars
               (make TEXT, model TEXT, quantity INT)
               """)

# close connection
conn.close()
