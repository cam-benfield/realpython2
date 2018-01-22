import sqlite3

with sqlite3.connect("new1.db") as connection:
    c = connection.cursor()

    data = [
            ("Ford", "Taurus", 6),
            ("Ford", "Focus", 2),
            ("Ford", "Explorer", 1),
            ("Honda", "Civic", 8),
            ("Honda", "Accord", 2)
            ]

    c.executemany('INSERT INTO cars VALUES (?, ?, ?)', data)
