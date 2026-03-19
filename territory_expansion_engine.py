import json
import random

TERRITORY_FILE = "data/territories.json"

def expand_polygon(polygon):
    expanded = []

    for lat, lon in polygon:
        lat += random.uniform(-10,10)
        lon += random.uniform(-10,10)
        expanded.append([lat, lon])

    return expanded


def expand_territories():

    with open(TERRITORY_FILE) as f:
        territories = json.load(f)


    for civ in territories:
        poly = territories[civ]["polygon"]
        territories[civ]["polygon"] = expand_polygon(poly)

    with open(TERRITORY_FILE, "w") as f:
        json.dump(territories, f, indent=2)

    return territories