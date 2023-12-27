import sqlite3
conn = sqlite3.connect("store.db")
db = conn.cursor()
db.execute("""CREATE TABLE IF NOT EXISTS books(
               id integer,
           name text
)""")

#db.execute("INSERT INTO books VALUES(7, 'Harry Potter and the Deathly Hallows')")
db.execute("SELECT * FROM books")
one = db.fetchall()
print(one)

conn.commit()
conn.close()