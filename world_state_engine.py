
"""
WORLD STATE ENGINE
Central authority for simulation memory
"""

import json
import os

WORLD_STATE = None


def load_world_state():
    global WORLD_STATE

    if WORLD_STATE is not None:
        return WORLD_STATE

    if os.path.exists("data/world_state.json"):
        with open("data/world_state.json") as f:
            WORLD_STATE = json.load(f)
    else:
        WORLD_STATE = {
            "turn": 0,
            "civilizations": {},
            "territories": {},
            "relationships": {},
            "contact_stages": {},
            "trade_routes": [],
            "conflicts": [],
            "chronicle": []
        }

    return WORLD_STATE


def save_world_state():
    os.makedirs("data", exist_ok=True)

    with open("data/world_state.json","w") as f:
        json.dump(WORLD_STATE,f,indent=2)


def get_world_state():
    return load_world_state()


def initialize_world(civilizations):
    state = load_world_state()

    for civ in civilizations:
        state["civilizations"][civ["name"]] = civ


def advance_turn():
    state = load_world_state()
    state["turn"] += 1


def record_event(text):
    state = load_world_state()
    state["chronicle"].append({
        "turn": state["turn"],
        "event": text
    })


def get_contact_stage(civ_a,civ_b):
    state = load_world_state()
    key = str(tuple(sorted([civ_a,civ_b])))
    return state["contact_stages"].get(key,"unknown")


def set_contact_stage(civ_a,civ_b,stage):
    state = load_world_state()
    key = str(tuple(sorted([civ_a,civ_b])))
    state["contact_stages"][key] = stage
