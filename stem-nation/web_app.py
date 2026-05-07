 
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



@app.route("/environment_entry")
def environment_entry():
    world = request.args.get("world", "river")
    return render_template("environment_entry.html", world=world)


# =========================
# ACADEMY (ZIP)
# =========================
@app.route("/academy_individual")
def academy_individual():
    return render_template("academy_individual.html")


@app.route("/academy_memory_preview")
def academy_memory_preview():
    return render_template("academy_memory_preview.html")

@app.route("/academy_role")
def academy_role():
    return render_template("academy_role.html")

@app.route("/academy_thinking")
def academy_thinking():
    return render_template("academy_thinking.html")

@app.route("/academy_decision")
def academy_decision():
    return render_template("academy_decision.html")



# =========================
# SAFE PLACEHOLDERS
# =========================
@app.route("/teacher")
def teacher():
    return render_template("teacher.html")
@app.route("/map")
def map_mode():
    return render_template("map_mode.html")
@app.route("/partners")
def partners():
    return render_template("partners.html")

@app.route("/region_river")
def region_river():
    return render_template("region_river.html")








@app.route("/week2_survival_archive")
def week2_survival_archive():
    return render_template("week2_survival_archive.html")

@app.route("/week2_survival_workspace")
def week2_survival_workspace():
    return render_template("week2_survival_workspace.html")

@app.route("/week2_survival_intro")
def week2_survival_intro():
    return render_template("week2_survival_intro.html")

@app.route("/founding_complete")
def founding_complete():
    return render_template("founding_complete.html")

@app.route("/founding_archive_print")
def founding_archive_print():
    return render_template("founding_archive_print.html")

@app.route("/hub")
def hub():
    return render_template("project_hub.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
