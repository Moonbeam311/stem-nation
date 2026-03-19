
"""
AUTO TURN ENGINE
Runs the full simulation loop automatically
"""

import time
import world_state_engine as world
import influence_engine
import contact_engine
import trade_engine
import conflict_engine


def run_turn():

    state = world.get_world_state()
    civilizations = list(state["civilizations"].values())

    world.advance_turn()

    influence_engine.apply_influence(civilizations)
    contact_engine.detect_contacts(civilizations)
    trade_engine.evaluate_trade(civilizations)
    conflict_engine.evaluate_conflicts(civilizations)

    world.save_world_state()

    print("Turn", state["turn"], "completed")


def run_simulation(turn_delay=3):

    print("Auto simulation started")

    while True:

        run_turn()

        time.sleep(turn_delay)
