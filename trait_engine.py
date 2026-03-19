def apply_environment_bonus(civ):

    env = getattr(civ, "environment", None)

    if env == "river":
        civ.food += 5

    elif env == "forest":
        civ.stability += 3

    elif env == "highland":
        civ.technology += 3

    elif env == "coastal":
        civ.wealth += 5

    elif env == "steppe":
        civ.population += 3

    elif env == "desert":
        civ.wealth += 2


def apply_trait_bonus(civ):

    traits = getattr(civ, "traits", [])

    for trait in traits:

        if trait == "builders":
            civ.stability += 2

        elif trait == "traders":
            civ.wealth += 3

        elif trait == "engineers":
            civ.technology += 2

        elif trait == "scholars":
            civ.technology += 3

        elif trait == "navigators":
            civ.wealth += 2

        elif trait == "diplomats":
            civ.stability += 2

        elif trait == "healers":
            civ.stability += 2

        elif trait == "warriors":
            civ.population += 2

        elif trait == "horse_lords":
            civ.population += 3

        elif trait == "organizers":
            civ.stability += 2

        elif trait == "metalworkers":
            civ.wealth += 2

        elif trait == "ritualists":
            civ.stability += 1
