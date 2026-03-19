import json


def load_artifacts():

    with open("data/artifacts.json") as f:
        data = json.load(f)

    return data["artifacts"]