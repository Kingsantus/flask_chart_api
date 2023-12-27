import sqlite3

connection = sqlite3.connect('store.db')

with open('store.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

#cursor.execute("INSERT INTO books (title) VALUES (?)", ("Harry Potter and the Soccerers Stone",))
#cursor.execute("INSERT INTO books (title) VALUES (?)", ('Harry Potter and the Chamber of Screts',))
#cursor.execute("INSERT INTO books (title) VALUES (?)", ('Harry Potter and the Prisoner of Azkaban',))
#cursor.execute("INSERT INTO books (title) VALUES (?)", ('Harry Potter and the Goblet of Fire',))
#cursor.execute("INSERT INTO books (title) VALUES (?)", ('Harry Potter and the Order of the Phoenix',))
#cursor.execute("INSERT INTO books (title) VALUES (?)", ('Harry Potter and the Half-Blood Prince',))
#cursor.execute("INSERT INTO books (title) VALUES (?)", ('Harry Potter and the Deathly Hallows',))

cursor.execute("SELECT * FROM books")
one = print(cursor.fetchall())

connection.commit()
connection.close()