# import sql
import sqlite3

# create connection
conn = sqlite3.connect("new.db")

# create cursor
cursor = conn.cursor()
try:
    # insert data
    cursor.execute("INSERT INTO population VALUES('New York City', \
    'NY', 8400000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco', \
    'CA', 800000)")

    # commit the changes
    conn.commit()

except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

# close the connection
conn.close()
