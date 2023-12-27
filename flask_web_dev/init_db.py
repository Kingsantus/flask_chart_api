import sqlite3

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("first post", "Content for the first post"))

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ("second post", "Content for the Second post"))

connection.commit()
connection.close()