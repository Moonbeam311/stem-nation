
"""
CONTACT ENGINE
Handles civilization encounters and relationship progression
"""

import random
import math
import world_state_engine as world


CONTACT_SEQUENCE = [
    "scouts",
    "first_contact",
    "trade",
    "tension",
    "war"
]


def distance(a, b):
    return math.sqrt((a["x"] - b["x"])**2 + (a["y"] - b["y"])**2)


def detect_contacts(civilizations):

    for i in range(len(civilizations)):
        for j in range(i + 1, len(civilizations)):

            civ_a = civilizations[i]
            civ_b = civilizations[j]

            d = distance(civ_a["capital"], civ_b["capital"])

            influence = civ_a["influence"] + civ_b["influence"]

            if d < influence:

                advance_contact(civ_a["name"], civ_b["name"])


def advance_contact(civ_a, civ_b):

    stage = world.get_contact_stage(civ_a, civ_b)

    if stage == "unknown":
        next_stage = CONTACT_SEQUENCE[0]

    else:
        idx = CONTACT_SEQUENCE.index(stage)

        if idx < len(CONTACT_SEQUENCE) - 1:
            next_stage = CONTACT_SEQUENCE[idx + 1]
        else:
            next_stage = stage

    world.set_contact_stage(civ_a, civ_b, next_stage)

    record_contact_event(civ_a, civ_b, next_stage)


def record_contact_event(a, b, stage):

    messages = {
        "scouts": f"Scouts from {a} sighted the lands of {b}.",
        "first_contact": f"Envoys from {a} and {b} established first contact.",
        "trade": f"Trade routes opened between {a} and {b}.",
        "tension": f"Border tensions rise between {a} and {b}.",
        "war": f"War erupts between {a} and {b}!"
    }

    world.record_event(messages[stage])


