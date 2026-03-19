import random
from artifact_registry import load_artifacts
from library_engine import add_artifact
from chronicle_engine import record_event


def attempt_exploration(civilizations, world_regions):

    hidden_regions = [r for r in world_regions if r["hidden"]]

    if not hidden_regions:
        return

    civ = random.choice(civilizations)

    region = random.choice(hidden_regions)

    region["hidden"] = False

    print("\nEXPLORATION DISCOVERY!")
    print(f"{civ.name} explorers discovered {region['name']}!")

    record_event("?", f"{civ.name} explorers discovered {region['name']}")

    artifacts = load_artifacts()

    if random.random() < 0.4:

        artifact = random.choice(artifacts)

        print("\nARTIFACT DISCOVERED!")
        print(artifact["name"])
        add_artifact(civ, artifact["name"])

        effect = artifact["effect"]

        if "food" in effect:
            civ.food += effect["food"]

        if "wealth" in effect:
            civ.wealth += effect["wealth"]

        if "technology" in effect:
            civ.technology += effect["technology"]

        if "stability" in effect:
            civ.stability += effect["stability"]

        record_event("?", f"{civ.name} discovered artifact {artifact['name']}")
