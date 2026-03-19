from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)

turn = 1
current_event = "Simulation begins"
chronicle = ["Turn 1 - Simulation begins"]

EVENTS = [
    "River Flood",
    "Trade Caravan",
    "Harvest Season",
    "Border Tension",
    "Diplomatic Envoys",
    "Scholar Gathering",
]

civilizations = {
    "Mississippian": {
        "population": 100, "food": 80, "wealth": 60,
        "technology": 40, "stability": 70, "influence": 50
    },
    "Susquehannock": {
        "population": 100, "food": 80, "wealth": 60,
        "technology": 40, "stability": 70, "influence": 50
    },
    "Inca": {
        "population": 100, "food": 80, "wealth": 60,
        "technology": 40, "stability": 70, "influence": 50
    },
    "Phoenician": {
        "population": 100, "food": 80, "wealth": 60,
        "technology": 40, "stability": 70, "influence": 50
    },
}

territories = [
    {"id": 1, "name": "River Valley", "lat": 35.0, "lng": -90.0, "owner": "Mississippian", "value": {"food": 4, "trade": 3, "defense": 2}},
    {"id": 2, "name": "Forest Belt", "lat": 40.0, "lng": -77.0, "owner": "Susquehannock", "value": {"food": 3, "trade": 2, "defense": 3}},
    {"id": 3, "name": "Highland Ridge", "lat": -13.5, "lng": -71.9, "owner": "Inca", "value": {"food": 2, "trade": 2, "defense": 4}},
    {"id": 4, "name": "Coastal Sea", "lat": 34.5, "lng": 35.9, "owner": "Phoenician", "value": {"food": 2, "trade": 4, "defense": 2}},
    {"id": 5, "name": "Central Basin", "lat": 32.0, "lng": -84.0, "owner": "Unclaimed", "value": {"food": 4, "trade": 1, "defense": 1}},
    {"id": 6, "name": "Trade Crossroads", "lat": 39.0, "lng": -95.0, "owner": "Unclaimed", "value": {"food": 2, "trade": 5, "defense": 1}},
    {"id": 7, "name": "Island Chain", "lat": 18.0, "lng": -66.0, "owner": "Unclaimed", "value": {"food": 2, "trade": 3, "defense": 2}},
]

def civ_color(owner):
    return {
        "Mississippian": "green",
        "Susquehannock": "blue",
        "Inca": "gold",
        "Phoenician": "red",
        "Unclaimed": "gray",
    }.get(owner, "gray")

def generate_advice(name, stats):
    notes = []
    if stats["food"] < 50:
        notes.append(f"{name}: Food is low. Prioritize agriculture or trade.")
    if stats["wealth"] < 40:
        notes.append(f"{name}: Wealth is limited. Strengthen trade and production.")
    if stats["technology"] < 35:
        notes.append(f"{name}: Knowledge development is lagging. Invest in research.")
    if stats["stability"] < 50:
        notes.append(f"{name}: Stability is weakening. Build and govern carefully.")
    if stats["influence"] > 70:
        notes.append(f"{name}: Influence is rising. Expansion opportunities are opening.")
    if not notes:
        notes.append(f"{name}: Civilization is stable. Maintain balanced growth.")
    return notes

def all_advice():
    out = []
    for name, stats in civilizations.items():
        out.extend(generate_advice(name, stats))
    return out

def leaderboard():
    ranked = []
    for name, s in civilizations.items():
        score = s["population"] + s["food"] + s["wealth"] + s["technology"] + s["stability"]
        ranked.append((name, score))
    return sorted(ranked, key=lambda x: x[1], reverse=True)

def apply_turn_drift():
    for stats in civilizations.values():
        stats["population"] = max(0, stats["population"] + random.randint(0, 4))
        stats["food"] = max(0, stats["food"] + random.randint(-5, 4))
        stats["wealth"] = max(0, stats["wealth"] + random.randint(-2, 4))
        stats["technology"] = max(0, stats["technology"] + random.randint(0, 2))
        stats["stability"] = max(0, min(100, stats["stability"] + random.randint(-2, 2)))
        stats["influence"] = max(0, stats["influence"] + random.randint(0, 2))

def apply_decision(civ_name, decision):
    s = civilizations[civ_name]
    if decision == "expand":
        s["influence"] += 5
        s["wealth"] = max(0, s["wealth"] - 2)
    elif decision == "trade":
        s["wealth"] += 8
        s["food"] += 3
    elif decision == "build":
        s["stability"] = min(100, s["stability"] + 5)
        s["wealth"] = max(0, s["wealth"] - 3)
    elif decision == "research":
        s["technology"] += 5
        s["wealth"] = max(0, s["wealth"] - 2)
    chronicle.append(f"Turn {turn} - {civ_name} chose to {decision}")

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template(
        "index.html",
        turn=turn,
        event=current_event,
        chronicle=chronicle[-12:][::-1],
        leaderboard=leaderboard(),
        advisors=all_advice(),
        civilizations=civilizations,
    )

@app.route("/advance_turn")
def advance_turn():
    global turn, current_event
    turn += 1
    current_event = random.choice(EVENTS)
    apply_turn_drift()
    chronicle.append(f"Turn {turn} - {current_event}")
    return redirect(url_for("dashboard"))

@app.route("/decision/<civ_name>/<choice>")
def make_decision(civ_name, choice):
    if civ_name in civilizations:
        apply_decision(civ_name, choice)
    return redirect(url_for("dashboard"))

@app.route("/map")
def map_view():
    decorated = []
    for t in territories:
        item = dict(t)
        item["color"] = civ_color(item["owner"])
        decorated.append(item)
    return render_template("map.html", territories=decorated, civ_names=list(civilizations.keys()))

@app.route("/territories")
def get_territories():
    decorated = []
    for t in territories:
        item = dict(t)
        item["color"] = civ_color(item["owner"])
        decorated.append(item)
    return jsonify(decorated)

@app.route("/claim", methods=["POST"])
def claim_region():
    data = request.get_json(silent=True) or {}
    region_name = data.get("region_name")
    owner = data.get("owner")
    if owner not in civilizations:
        return jsonify({"ok": False, "error": "invalid owner"}), 400
    for t in territories:
        if t["name"] == region_name:
            if t["owner"] != "Unclaimed":
                return jsonify({"ok": False, "error": "already claimed", "region": t}), 409
            t["owner"] = owner
            chronicle.append(f"Turn {turn} - {owner} claims {region_name}")
            return jsonify({"ok": True, "region": t})
    return jsonify({"ok": False, "error": "region not found"}), 404

@app.route("/teacher")
def teacher():
    return render_template("teacher.html")

@app.route("/lessons")
def lessons():
    return render_template("lessons.html")

@app.route("/archive")
def archive():
    return render_template("archive.html", chronicle=chronicle[::-1])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
