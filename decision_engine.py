# COMPATIBLE DECISION ENGINE

def clear_decisions():
    return

def ensure_attr(civ, name, default):
    if not hasattr(civ, name):
        setattr(civ, name, default)

def apply_decision(civilization, decision):
    ensure_attr(civilization, "population", 100)
    ensure_attr(civilization, "food", 80)
    ensure_attr(civilization, "wealth", 60)
    ensure_attr(civilization, "technology", 40)
    ensure_attr(civilization, "stability", 70)
    ensure_attr(civilization, "influence", 50)

    if decision == "expand":
        civilization.influence += 5
        civilization.wealth = max(0, civilization.wealth - 2)

    elif decision == "trade":
        civilization.wealth += 8
        civilization.food += 3

    elif decision == "build":
        civilization.stability = min(100, civilization.stability + 5)
        civilization.wealth = max(0, civilization.wealth - 3)

    elif decision == "research":
        civilization.technology += 5
        civilization.wealth = max(0, civilization.wealth - 2)

    return f"{civilization.name} chose to {decision}"
