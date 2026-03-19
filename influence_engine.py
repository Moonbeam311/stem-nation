
"""
INFLUENCE ENGINE
Civilization expansion based on influence radius
"""

import random
import world_state_engine as world


def apply_influence(civilizations):
    state = world.get_world_state()

    territories = state["territories"]

    for civ in civilizations:

        name = civ["name"]
        capital = civ["capital"]
        influence = civ["influence"]

        if name not in territories:
            territories[name] = []

        # grow influence
        for _ in range(random.randint(1,3)):

            x = capital["x"] + random.uniform(-influence, influence)
            y = capital["y"] + random.uniform(-influence, influence)

            territories[name].append([x, y])

        world.record_event(f"{name} expands its influence.")
