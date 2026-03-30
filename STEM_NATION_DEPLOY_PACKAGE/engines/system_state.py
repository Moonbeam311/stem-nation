# SYSTEM STATE (GLOBAL SESSION MEMORY)

state = {
    "selected_region": None,
    "population": 10,
    "food": 5,
    "shelter": 5,
    "knowledge": 0,
    "stability": 5
}


def update_state(changes):
    for key, value in changes.items():
        if key in state:
            state[key] += value


def get_state():
    return state
