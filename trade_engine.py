
"""
TRADE ENGINE
Creates trade routes between civilizations that have reached first contact
"""

import random
import world_state_engine as world


def evaluate_trade(civilizations):

    state = world.get_world_state()

    contacts = state["contact_stages"]

    for pair, stage in contacts.items():

        civ_a, civ_b = eval(pair)

        if stage == "first_contact":

            # 50% chance to begin trade
            if random.random() < 0.5:

                route = (civ_a, civ_b)

                if route not in state["trade_routes"]:

                    state["trade_routes"].append(route)

                    world.record_event(
                        f"Trade route established between {civ_a} and {civ_b}."
                    )
