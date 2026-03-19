from flask import Flask, render_template, redirect, url_for, request
from civilization_engine import Civilization
from event_engine import generate_event, events
from session_manager import create_session, join_session

app = Flask(__name__)

turn = 1
current_event = "Simulation begins"

chronicle = ["Turn 1 — Simulation begins"]

session_code = None

civilizations = [
    Civilization("River Alliance"),
    Civilization("Forest Union"),
    Civilization("Highland Confederacy"),
    Civilization("Coastal League")
]

world_map = {
    "Forest Belt": "Forest Union",
    "River Corridor": "River Alliance",
    "Highland Ridge": "Highland Confederacy",
    "Valley Basin": "Coastal League"
}

simulation_active = True


@app.route("/")
def dashboard():

    civ_data = []

    for civ in civilizations:
        civ_data.append({
            "name": civ.name,
            "population": civ.population,
            "food": civ.food,
            "wealth": civ.wealth,
            "technology": civ.technology,
            "stability": civ.stability
        })

    return render_template(
        "index.html",
        turn=turn,
        civilizations=civ_data,
        world_map=world_map,
        event=current_event,
        chronicle=chronicle,
        events=events,
        active=simulation_active,
        session_code=session_code
    )


@app.route("/create_session")
def create_classroom_session():

    global session_code

    session_code = create_session()

    chronicle.append(f"Classroom Session Created — Code {session_code}")

    return redirect(url_for("dashboard"))


@app.route("/join")
def join_page():

    return render_template("student_join.html")


@app.route("/join_session", methods=["POST"])
def join_classroom():

    code = request.form["code"]
    name = request.form["name"]
    civilization = request.form["civilization"]

    success = join_session(code, name, civilization)

    if success:
        chronicle.append(f"{name} joined {civilization} in session {code}")
    else:
        chronicle.append(f"Join failed for {name}")

    return redirect(url_for("join_page"))


@app.route("/advance_turn")
def advance_turn():

    global turn, current_event

    if not simulation_active:
        return redirect(url_for("dashboard"))

    turn += 1

    current_event = generate_event()

    for civ in civilizations:

        civ.population += 1
        civ.food -= 1
        civ.wealth += 2
        civ.technology += 1

        civ.apply_event(current_event)

    chronicle.append(f"Turn {turn} — {current_event}")

    return redirect(url_for("dashboard"))


@app.route("/inject/<event_name>")
def inject_event(event_name):

    global current_event

    current_event = event_name

    for civ in civilizations:
        civ.apply_event(event_name)

    chronicle.append(f"Teacher Event — {event_name}")

    return redirect(url_for("dashboard"))


@app.route("/end_simulation")
def end_simulation():

    global simulation_active

    simulation_active = False
    chronicle.append("Simulation ended by teacher")

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
