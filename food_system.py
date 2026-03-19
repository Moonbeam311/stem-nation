"""
Food Production System
Nation Builder Engine
"""

import random


def produce_food(civilization):

    farmers = civilization.labor.get("farmers", 0)

    # each farmer produces food
    harvest = farmers * random.randint(1, 3)

    civilization.food += harvest

    return harvest


def consume_food(civilization):

    consumption = civilization.population

    civilization.food -= consumption

    if civilization.food < 0:
        civilization.stability -= 2
        civilization.food = 0


def apply_food_cycle(civilization):

    harvest = produce_food(civilization)

    consume_food(civilization)

    return harvest
