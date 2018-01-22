import sqlite3

with sqlite3.connect("new1.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders
    (make TEXT, model TEXT, order_date DATE)""")

    orders = [
        ('Ford', 'Taurus', '2017-07-09'),
        ('Ford', 'Focus', '2017-10-31'),
        ('Ford', 'Taurus', '2017-12-01'),
        ('Ford', 'Taurus', '2017-07-14'),
        ('Honda', 'Civic', '2016-03-14'),
        ('Honda', 'Civic', '2016-03-23'),
        ('Honda', 'Civic', '2016-03-31'),
        ('Ford', 'Focus', '2017-09-17'),
        ('Ford', 'Focus', '2017-09-23'),
        ('Ford', 'Explorer', '2016-01-12'),
        ('Ford', 'Explorer', '2016-12-12'),
        ('Ford', 'Explorer', '2016-11-12'),
        ('Honda', 'Accord', '2017-12-12'),
        ('Honda', 'Accord', '2017-08-13'),
        ('Honda', 'Accord', '2017-11-27')
    ]

    c.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders)

    c.execute("SELECT * FROM orders")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
