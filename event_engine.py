import random

events = [
    "River Flood",
    "Trade Caravan",
    "Harvest Festival",
    "Border Dispute",
    "Mine Discovery"
]

def generate_event():
    return random.choice(events)