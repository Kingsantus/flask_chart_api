import sqlite3

conn = sqlite3.connect("info.db")
db = conn.cursor()


db.execute("""CREATE TABLE IF NOT EXISTS shows (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           title TEXT
    )
""")

conn.commit()
conn.close()