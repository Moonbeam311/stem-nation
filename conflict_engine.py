
"""
CONFLICT ENGINE
Escalates tensions and creates wars between civilizations
"""

import random
import world_state_engine as world


def evaluate_conflicts(civilizations):

    state = world.get_world_state()

    contacts = state["contact_stages"]

    for pair, stage in list(contacts.items()):

        civ_a, civ_b = eval(pair)

        # escalate from trade to tension
        if stage == "trade":

            if random.random() < 0.3:

                world.set_contact_stage(civ_a, civ_b, "tension")

                world.record_event(
                    f"Tensions rise between {civ_a} and {civ_b}."
                )

        # escalate from tension to war
        elif stage == "tension":

            if random.random() < 0.2:

                state["conflicts"].append((civ_a, civ_b))

                world.set_contact_stage(civ_a, civ_b, "war")

                world.record_event(
                    f"War erupts between {civ_a} and {civ_b}."
                )
