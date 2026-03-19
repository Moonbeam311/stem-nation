import json


def load_civilizations():

    with open("data/civilizations.json") as f:
        data = json.load(f)

    return data["civilizations"]