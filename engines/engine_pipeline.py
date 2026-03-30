from engines.system_state import session

def apply_decision(decision):
    for key, value in decision["effects"].items():
        if key in session:
            session[key] += value

    session["score"] += sum(decision["effects"].values())

    session["scrolls"].append({
        "type": "decision",
        "decision": decision["id"],
        "effects": decision["effects"]
    })

    update_totem()

def update_totem():
    if session["unity"] > 7:
        session["totem_level"] = "community_builder"
    elif session["knowledge"] > 7:
        session["totem_level"] = "keeper_of_memory"
