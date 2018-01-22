import sqlite3

with sqlite3.connect("new1.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE cars SET quantity=5 WHERE make='Ford' and\
        model='Taurus'")
    c.execute("UPDATE cars SET quantity=7 WHERE make='Honda' and\
        model='Civic'")

    c.execute('SELECT * from cars')

    cars = c.fetchall()

    for r in cars:
        print(r[0], r[1], r[2])
