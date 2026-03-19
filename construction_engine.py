
"""
Construction System
Nation Builder Engine
"""

def build_structure(civilization, structure):

    # guarantee infrastructure exists
    if not hasattr(civilization, "infrastructure"):
        civilization.infrastructure = {
            "farms": 0,
            "roads": 0,
            "markets": 0,
            "academies": 0,
            "walls": 0
        }

    if structure not in civilization.infrastructure:
        return False

    civilization.infrastructure[structure] += 1

    if structure == "farms":
        civilization.food += 20

    elif structure == "markets":
        civilization.wealth += 10

    elif structure == "academies":
        civilization.technology += 5

    elif structure == "walls":
        civilization.stability += 3

    return True
