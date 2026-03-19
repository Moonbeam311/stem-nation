"""
DECISION ROUTER
Maps classroom decisions into simulation inputs
"""

def route_decision(decision, civ):
    if decision == "agriculture":
        civ["food"] = civ.get("food", 0) + 10

    elif decision == "trade":
        civ["wealth"] = civ.get("wealth", 0) + 10

    elif decision == "research":
        civ["technology"] = civ.get("technology", 0) + 10

    elif decision == "infrastructure":
        civ["construction"] = civ.get("construction", 0) + 5

    elif decision == "stability":
        civ["stability"] = civ.get("stability", 0) + 5

    return civ
