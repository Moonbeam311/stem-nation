from flask import Flask, render_template, redirect, url_for, jsonify, request
from civilization_engine import Civilization
from advisor_system import generate_advice
from decision_engine import apply_decision
import random

app = Flask(__name__)

# ------------------------------
# WORLD STATE
# ------------------------------

turn = 1
current_event = "Simulation begins"
chronicle = ["Turn 1 - Simulation begins"]
advisor_messages = []

EVENTS = [
    "River Flood",
    "Trade Caravan",
    "Harvest Season",
    "Border Tension",
    "Diplomatic Envoys",
    "Scholar Gathering",
]

def make_civ(name: str):
    civ = Civilization(name)
    defaults = {
        "population": 100,
        "food": 80,
        "wealth": 60,
        "technology": 40,
        "stability": 70,
        "influence": 50,
    }
    for k, v in defaults.items():
        if not hasattr(civ, k):
            setattr(civ, k, v)
    return civ

civilizations = [
    make_civ("Mississippian"),
    make_civ("Susquehannock"),
    make_civ("Inca"),
    make_civ("Phoenician"),
]

world_map = [
    {"name": "River Valley", "owner": "Mississippian"},
    {"name": "Forest Belt", "owner": "Susquehannock"},
    {"name": "Highland Ridge", "owner": "Inca"},
    {"name": "Coastal Sea", "owner": "Phoenician"},
    {"name": "Central Basin", "owner": "Unclaimed"},
    {"name": "Trade Crossroads", "owner": "Unclaimed"},
    {"name": "Island Chain", "owner": "Unclaimed"},
]

def leaderboard_for(civs):
    scored = []
    for civ in civs:
        score = (
            getattr(civ, "population", 0)
            + getattr(civ, "food", 0)
            + getattr(civ, "wealth", 0)
            + getattr(civ, "technology", 0)
            + getattr(civ, "stability", 0)
        )
        scored.append((civ.name, score))
    return sorted(scored, key=lambda x: x[1], reverse=True)

def apply_turn_drift():
    for civ in civilizations:
        civ.population = max(0, getattr(civ, "population", 0) + random.randint(0, 4))
        civ.food = max(0, getattr(civ, "food", 0) + random.randint(-5, 4))
        civ.wealth = max(0, getattr(civ, "wealth", 0) + random.randint(-2, 4))
        civ.technology = max(0, getattr(civ, "technology", 0) + random.randint(0, 2))
        civ.stability = max(0, min(100, getattr(civ, "stability", 0) + random.randint(-2, 2)))
        civ.influence = max(0, getattr(civ, "influence", 0) + random.randint(0, 2))

@app.route("/")
def index():
    return render_template(
        "index.html",
        turn=turn,
        event=current_event,
        chronicle=chronicle,
        leaderboard=leaderboard_for(civilizations),
        advisors=advisor_messages,
        world_map=world_map,
        civilizations=civilizations,
    )

@app.route("/advance_turn")
def advance_turn():
    global turn, current_event, advisor_messages

    turn += 1
    current_event = random.choice(EVENTS)
    apply_turn_drift()

    advisor_messages = []
    for civ in civilizations:
        advisor_messages.extend(generate_advice(civ))

    chronicle.append(f"Turn {turn} - {current_event}")
    return redirect(url_for("index"))

@app.route("/decision/<civ_name>/<choice>")
def make_decision(civ_name, choice):
    global chronicle

    civ = next((c for c in civilizations if c.name == civ_name), None)
    if civ is None:
        return redirect(url_for("index"))

    result = apply_decision(civ, choice)
    chronicle.append(f"Turn {turn} - {result}")

    advisor_messages.clear()
    for c in civilizations:
        advisor_messages.extend(generate_advice(c))

    return redirect(url_for("index"))

@app.route("/map")
def map_view():
    return render_template(
        "map.html",
        regions=world_map,
        civ_names=[c.name for c in civilizations]
    )

@app.route("/territories")
def get_territories():
    return jsonify(world_map)

@app.route("/claim", methods=["POST"])
def claim_region():
    data = request.get_json(silent=True) or {}
    region_name = data.get("region_name")
    owner = data.get("owner")

    valid_owners = {c.name for c in civilizations}
    if owner not in valid_owners:
        return jsonify({"ok": False, "error": "invalid owner"}), 400

    for r in world_map:
        if r["name"] == region_name:
            if r["owner"] == "Unclaimed":
                r["owner"] = owner
                chronicle.append(f"Turn {turn} - {owner} claims {region_name}")
                return jsonify({"ok": True, "region": r})
            return jsonify({"ok": False, "error": "already claimed", "region": r}), 409

    return jsonify({"ok": False, "error": "region not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
