
"""
CHRONICLE VIEWER
Displays world history from world_state.json
"""

import world_state_engine as world


def display_chronicle():

    state = world.get_world_state()
    chronicle = state.get("chronicle", [])

    print("\n==============================")
    print("STEM NATION CHRONICLE")
    print("==============================\n")

    if not chronicle:
        print("No historical events recorded yet.")
        return

    for entry in chronicle:
        turn = entry.get("turn", "?")
        event = entry.get("event", "")
        print(f"Turn {turn} - {event}")
