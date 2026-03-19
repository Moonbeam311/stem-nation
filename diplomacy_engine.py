import random

alliances = []


def attempt_diplomacy(civilizations):

    civ_names = [civ.name for civ in civilizations]

    if len(civ_names) < 2:
        return

    civ_a, civ_b = random.sample(civ_names, 2)

    pair = tuple(sorted([civ_a, civ_b]))

    if pair not in alliances and random.random() < 0.25:

        alliances.append(pair)

        print(f"Diplomatic Alliance Formed: {civ_a} and {civ_b}")

    elif pair in alliances and random.random() < 0.10:

        alliances.remove(pair)

        print(f"Alliance Broken: {civ_a} and {civ_b}")


def apply_alliance_bonuses(civilizations):

    for civ in civilizations:

        for a, b in alliances:

            if civ.name == a or civ.name == b:

                civ.wealth += 5

# ------------------------------------------------
# AUT0MAN COMPATIBILITY ADAPTER
# Ensures web_app.py can import form_alliance()
# ------------------------------------------------

def form_alliance(civ_a, civ_b, chronicle=None):
    """
    Compatibility wrapper for web layer.
    Attempts to create an alliance between two civilizations.
    """

    try:
        from random import random

        # basic probabilistic alliance formation
        if random() < 0.4:

            if hasattr(civ_a, "alliances"):
                civ_a.alliances.add(civ_b.name)

            if hasattr(civ_b, "alliances"):
                civ_b.alliances.add(civ_a.name)

            if chronicle:
                try:
                    chronicle.record(f"{civ_a.name} formed an alliance with {civ_b.name}")
                except:
                    pass

            return True

    except Exception:
        pass

    return False

