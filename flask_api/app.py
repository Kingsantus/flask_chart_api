import sqlite3
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

def get_db_connection():
    db = sqlite3.connect("info.db")
    db.row_factory = sqlite3.Row
    return db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    #shows = db.execute("SELECT * FROM shows WHERE title LIKE ?", "%" + request.args.get("q") + "%")
    #return render_template("search.html", shows=shows)
    q = request.args.get("q")
    if q:
        db = get_db_connection()
        shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", ("%" + q + "%",)).fetchall()
        db.close()
    else:
        shows = []
    return render_template("search.html", shows=shows)