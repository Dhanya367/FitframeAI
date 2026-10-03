import sqlite3
import os
import secrets
from flask import Flask, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from body_analysis import analyze, AnalysisError
from recommendations import RECS, get_recommendations

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["MAX_CONTENT_LENGTH"] = 15 * 1024 * 1024
DB = "database.db"


def init_db():
    with sqlite3.connect(DB) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created TEXT DEFAULT CURRENT_TIMESTAMP, user_id INTEGER,
            name TEXT, body_type TEXT, style_preference TEXT, shoulder REAL, waist REAL, hip REAL)""")
        cols = [row[1] for row in c.execute("PRAGMA table_info(results)").fetchall()]
        if "style_preference" not in cols:
            c.execute("ALTER TABLE results ADD COLUMN style_preference TEXT")
        if "user_id" not in cols:
            c.execute("ALTER TABLE results ADD COLUMN user_id INTEGER")
        c.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL)""")


init_db()


@app.route("/")
def home():
    return render_template("home.html")


def safe_next_path():
    path = request.args.get("next", "")
    return path if path.startswith("/") and not path.startswith("//") else url_for("start")


@app.route("/login", methods=["GET", "POST"], endpoint="login")
@app.route("/register", methods=["GET", "POST"], endpoint="register")
def authenticate():
    mode = "register" if request.path == "/register" else "login"
    show_lamp = mode == "register" or request.values.get("lamp") == "1"
    lamp_lit = show_lamp and request.method == "POST"
    if request.method == "GET":
        if session.get("user_id"):
            return redirect(url_for("start"))
        return render_template("login.html", mode=mode, error=None, next_path=safe_next_path(), show_lamp=show_lamp, lamp_lit=False)

    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    next_path = request.form.get("next", "")
    destination = next_path if next_path.startswith("/") and not next_path.startswith("//") else url_for("start")

    if "@" not in email or len(email) > 254:
        return render_template("login.html", mode=mode, error="Enter a valid email address.", next_path=destination, show_lamp=show_lamp, lamp_lit=lamp_lit), 400
    if mode == "register":
        if len(password) < 8:
            return render_template("login.html", mode=mode, error="Use a password with at least 8 characters.", next_path=destination, show_lamp=show_lamp, lamp_lit=lamp_lit), 400
        if password != request.form.get("confirm_password", ""):
            return render_template("login.html", mode=mode, error="Those passwords do not match.", next_path=destination, show_lamp=show_lamp, lamp_lit=lamp_lit), 400
        try:
            with sqlite3.connect(DB) as c:
                cursor = c.execute(
                    "INSERT INTO users(email, password_hash) VALUES(?, ?)",
                    (email, generate_password_hash(password)),
                )
                user_id = cursor.lastrowid
        except sqlite3.IntegrityError:
            return render_template("login.html", mode=mode, error="An account already exists for that email.", next_path=destination, show_lamp=show_lamp, lamp_lit=lamp_lit), 400
    else:
        with sqlite3.connect(DB) as c:
            user = c.execute("SELECT id, password_hash FROM users WHERE email = ?", (email,)).fetchone()
        if not user or not check_password_hash(user[1], password):
            return render_template("login.html", mode=mode, error="Email or password is incorrect.", next_path=destination, show_lamp=show_lamp, lamp_lit=lamp_lit), 400
        user_id = user[0]

    session.clear()
    session["user_id"] = user_id
    session["email"] = email
    return redirect(destination)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/start")
def start():
    if not session.get("user_id"):
        return redirect(url_for("login", next=request.path))
    return render_template("index.html", error=None)


@app.route("/analyze", methods=["POST"])
def analyze_route():
    if not session.get("user_id"):
        return redirect(url_for("login", next=url_for("start")))
    front, side = request.files.get("front"), request.files.get("side")
    name = request.form.get("name", "").strip() or "Guest"
    style = request.form.get("style_preference", "").strip()
    if not front or not front.filename:
        return render_template("index.html", error="Please upload a front photo."), 400
    if not style:
        return render_template("index.html", error="Please choose a style preference."), 400
    try:
        height = float(request.form.get("height", ""))
    except ValueError:
        height = 0
    if not 100 <= height <= 230:
        return render_template("index.html", error="Please enter your height in cm (100 to 230)."), 400
    try:
        res = analyze(front.read(), side.read() if side and side.filename else None, height)
    except AnalysisError as e:
        return render_template("index.html", error=str(e)), 400
    rec = get_recommendations(res["body_type"], style, height)
    with sqlite3.connect(DB) as c:
        c.execute("INSERT INTO results(user_id, name, body_type, style_preference, shoulder, waist, hip) VALUES(?,?,?,?,?,?,?)",
              (session["user_id"], name, res["body_type"], style, res["shoulder_cm"], res["waist_cm"], res["hip_cm"]))
    return render_template("result.html", name=name, style_preference=style, r=res, rec=rec, recs=RECS)


@app.route("/history")
def history():
    if not session.get("user_id"):
        return redirect(url_for("login", next=request.path))
    with sqlite3.connect(DB) as c:
        rows = c.execute("SELECT created, name, body_type FROM results WHERE user_id = ? ORDER BY id DESC LIMIT 50",
                         (session["user_id"],)).fetchall()
    return render_template("history.html", rows=rows)

init_db()

if __name__ == "__main__":
    app.run(debug=True)
