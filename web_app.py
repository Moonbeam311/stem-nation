import os

from engines.engine_pipeline import apply_decision
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/decision_bridge.html")
def decision_bridge():
    return render_template("decision_bridge.html")


# =========================
# ZIP ENTRY (UNCHANGED)
# =========================
@app.route("/")
def landing():
    return render_template("landing.html")


# =========================
# CINEMATIC (ZIP FILES)
# =========================
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


# =========================
# WORLD SELECT (ZIP)
# =========================
@app.route("/world_select.html")
def world_select():
    return render_template("world_select.html")


# =========================
# 🔥 CONNECT TO NEW BUILD
# =========================
@app.route("/region_experience")
def region_experience():
    region = request.args.get("region", "forest")
    return render_template("region_experience.html", region=region)


# =========================
# ACADEMY (ZIP)
# =========================
@app.route("/academy_individual")
def academy_individual():
    return render_template("academy_individual.html")

@app.route("/academy_role")
def academy_role():
    return render_template("academy_role.html")

@app.route("/academy_thinking")
def academy_thinking():
    return render_template("academy_thinking.html")

@app.route("/academy_decision")
def academy_decision():
    from engines.engine_pipeline import apply_decision

    decision = {
        "id": "expand_farming",
        "effects": {
            "food": 3,
            "economy": 1,
            "stability": -1,
            "unity": -1
        }
    }

    apply_decision(decision)

    return render_template("academy_decision.html")



# =========================
# SAFE PLACEHOLDERS
# =========================
@app.route("/teacher")
def teacher():
    return "<h1>Teacher Flow (not connected yet)</h1>"

@app.route("/map")
def map_mode():
    return "<h1>Simulation Mode (not connected yet)</h1>"

@app.route("/partners")
def partners():
    return "<h1>Partnerships (not connected yet)</h1>"

@app.route("/region_river")
def region_river():
    return render_template("region_river.html")


@app.route("/decision", methods=["POST"])

@app.route("/hub")
def hub():
    return render_template("project_hub.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

    app.run(debug=True)
