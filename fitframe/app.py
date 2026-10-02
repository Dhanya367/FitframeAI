import sqlite3
from flask import Flask, render_template, request
from body_analysis import analyze, AnalysisError
from recommendations import RECS, get_recommendations

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 15 * 1024 * 1024
DB = "database.db"


def init_db():
    with sqlite3.connect(DB) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created TEXT DEFAULT CURRENT_TIMESTAMP,
            name TEXT, body_type TEXT, style_preference TEXT, shoulder REAL, waist REAL, hip REAL)""")
        cols = [row[1] for row in c.execute("PRAGMA table_info(results)").fetchall()]
        if "style_preference" not in cols:
            c.execute("ALTER TABLE results ADD COLUMN style_preference TEXT")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/start")
def start():
    return render_template("index.html", error=None)


@app.route("/analyze", methods=["POST"])
def analyze_route():
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
        c.execute("INSERT INTO results(name, body_type, style_preference, shoulder, waist, hip) VALUES(?,?,?,?,?,?)",
                  (name, res["body_type"], style, res["shoulder_cm"], res["waist_cm"], res["hip_cm"]))
    return render_template("result.html", name=name, style_preference=style, r=res, rec=rec, recs=RECS)


@app.route("/history")
def history():
    with sqlite3.connect(DB) as c:
        rows = c.execute("SELECT created, name, body_type FROM results ORDER BY id DESC LIMIT 50").fetchall()
    return render_template("history.html", rows=rows)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
