from flask import Flask, redirect, render_template, request, session
import sqlite3
from flask_session import Session

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    return conn

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template("books.html", books=books)

@app.route("/cart", methods=["GET", "POST"])
def cart():
    #ensure if cart exists
    if "cart" not in session:
        session["cart"] = []

    #POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")
    
    #GET
    conn = get_db_connection()
    # Assuming session["cart"] is a list of IDs
    placeholders = ", ".join("?" for _ in session["cart"])
    query = f"SELECT * FROM books WHERE id IN ({placeholders})"
    books = conn.execute(query, session["cart"]).fetchall()
    conn.close()

    return render_template("cart.html", books=books)


