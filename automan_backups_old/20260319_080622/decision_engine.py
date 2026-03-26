
# ------------------------------------------------
# DECISION ENGINE — COMPATIBLE + EXTENDED
# ------------------------------------------------

def clear_decisions():
    """
    Placeholder for compatibility with existing system.
    """
    return


def apply_decision(civilization, decision):

    if decision == "expand":
        civilization.influence += 5
        civilization.wealth -= 2

    elif decision == "trade":
        civilization.wealth += 5
        civilization.food += 2

    elif decision == "build":
        civilization.stability += 5
        civilization.wealth -= 3

    elif decision == "research":
        civilization.technology += 5
        civilization.wealth -= 2

    return f"{civilization.name} chose to {decision}"


# ------------------------------------------------
# TERRITORY CLAIM LOGIC
# ------------------------------------------------
def claim_territory(civilization, world_map, chronicle):

    unclaimed = [r for r in world_map if r["owner"] is None]

    if not unclaimed:
        chronicle.append(f"{civilization.name} attempted expansion, but no land remains")
        return

    region = unclaimed[0]  # simple for now

    region["owner"] = civilization.name

    chronicle.append(f"{civilization.name} claims {region['name']}")
