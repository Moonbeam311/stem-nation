from flask import Flask, render_template, redirect, url_for, jsonify

from civilization_engine import Civilization
from event_engine import generate_event
from advisor_system import generate_advice
from leaderboard_engine import generate_leaderboard
from population_engine import initialize_population
from decision_engine import clear_decisions, apply_decision

app = Flask(__name__)

# ------------------------------
# WORLD STATE
# ------------------------------

turn = 1
current_event = "Simulation begins"

chronicle = ["Turn 1 — Simulation begins"]
advisor_messages = []

civilizations = [
    Civilization("Mississippian"),
    Civilization("Susquehannock"),
    Civilization("Inca"),
    Civilization("Phoenician")
]

# Initialize populations
for civ in civilizations:
    initialize_population(civ)

# ------------------------------
# MAP
# ------------------------------

world_map = [
    {"name": "River Valley", "owner": None},
    {"name": "Forest Belt", "owner": None},
    {"name": "Highland Ridge", "owner": None},
    {"name": "Coastal Sea", "owner": None},
    {"name": "Central Basin", "owner": None},
    {"name": "Trade Crossroads", "owner": None},
    {"name": "Island Chain", "owner": None},
]

for civ, region in zip(civilizations, world_map):
    region["owner"] = civ.name

# ------------------------------
# ROUTES
# ------------------------------

@app.route("/")
def index():
    leaderboard = generate_leaderboard(civilizations)
    world_map_dict = {r["name"]: r["owner"] for r in world_map}

    return render_template(
        "index.html",
        turn=turn,
        event=current_event,
        chronicle=chronicle,
        leaderboard=leaderboard,
        advisors=advisor_messages,
        world_map=world_map_dict,
        civilizations=civilizations
    )


@app.route("/advance_turn")
def advance_turn():
    global turn, current_event, advisor_messages

    turn += 1
    current_event = generate_event()

    advisor_messages = []
    for civ in civilizations:
        advisor_messages.extend(generate_advice(civ))

    chronicle.append(f"Turn {turn} — {current_event}")

    return redirect(url_for("index"))


@app.route("/decision/<civ_name>/<choice>")
def make_decision(civ_name, choice):
    global chronicle

    for civ in civilizations:
        if civ.name == civ_name:
            result = apply_decision(civ, choice)
            chronicle.append(f"Turn {turn} — {result}")
            break

    return redirect(url_for("index"))




@app.route("/map")
def map_view():
    return render_template("map.html", regions=world_map)



# ------------------------------------------------
# TERRITORY API
# ------------------------------------------------



# ------------------------------------------------
# TERRITORY API
# ------------------------------------------------



# TERRITORY API

# TERRITORY API





@app.route("/territories")
def get_territories():
    return jsonify(world_map)



@app.route("/claim/<region_name>")
def claim_region(region_name):
    for r in world_map:
        if r["name"] == region_name and (r["owner"] is None or r["owner"] == "Unclaimed"):
            r["owner"] = "Mississippian"  # default player for now
    return ("OK", 200)

if __name__ == "__main__":
    app.run(debug=True)