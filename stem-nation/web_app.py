from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- LANDING ----------------
@app.route("/")
def landing():
    return render_template("landing.html")

# ---------------- CINEMATIC ----------------
@app.route("/intro1")
def intro1():
    return render_template("intro1.html")

@app.route("/intro2")
def intro2():
    return render_template("intro2.html")

@app.route("/intro3")
def intro3():
    return render_template("intro3.html")

@app.route("/intro4")
def intro4():
    return render_template("intro4.html")

@app.route("/intro5")
def intro5():
    return render_template("intro5.html")

# ---------------- WORLD ----------------
@app.route("/world_select.html")
def world_select():
    return render_template("world_select.html")

# ---------------- ACADEMY ENGINE ----------------
@app.route("/academy_individual")
def academy_individual():
    world = request.args.get("world", "unknown")
    return render_template("academy_individual.html", world=world)

@app.route("/academy_role")
def academy_role():
    world = request.args.get("world", "unknown")
    return render_template("academy_role.html", world=world)

@app.route("/academy_thinking")
def academy_thinking():
    world = request.args.get("world", "unknown")
    return render_template("academy_thinking.html", world=world)

@app.route("/academy_decision")
def academy_decision():
    world = request.args.get("world", "unknown")
    return render_template("academy_decision.html", world=world)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)


