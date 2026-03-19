"""
Population Labor System
Nation Builder Engine
"""

import random


def initialize_population(civilization):

    population = civilization.population

    civilization.labor = {
        "farmers": int(population * 0.4),
        "builders": int(population * 0.2),
        "traders": int(population * 0.15),
        "scholars": int(population * 0.15),
        "defenders": int(population * 0.1),
    }


def update_population(civilization):

    growth = random.randint(1, 5)

    civilization.population += growth

    if hasattr(civilization, "labor"):
        civilization.labor["farmers"] += 1


def get_labor_summary(civilization):

    if not hasattr(civilization, "labor"):
        initialize_population(civilization)

    return civilization.labor
