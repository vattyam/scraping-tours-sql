import sqlite3


# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query the data
cursor.execute("SELECT * FROM events WHERE band='Monkey'")
rows = cursor.fetchall()
print(rows)

# Query certain columns
cursor.execute("SELECT band, date FROM events WHERE band='Monkey'")
rows = cursor.fetchall()
print(rows)

#Insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.17'),
            ('Hens', 'Hen City', '2024.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows)
connection.commit()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
