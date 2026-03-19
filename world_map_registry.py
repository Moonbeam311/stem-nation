import json


def load_world_map():

    with open("data/world_map.json") as f:
        data = json.load(f)

    return data["regions"]