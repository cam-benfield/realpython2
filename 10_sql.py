import sqlite3

with sqlite3.connect("new1.db") as connection:
    c = connection.cursor()
    c.execute("SELECT * FROM cars WHERE make='Ford'")
    cars = c.fetchall()
    for r in cars:
        print(r[0], r[1], r[2])
