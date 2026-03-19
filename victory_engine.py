
def check_victory(civilizations):

    for civilization in civilizations:

        if civilization.wealth >= 500:
            return civilization.name + " achieved Economic Dominance"

        if civilization.technology >= 500:
            return civilization.name + " achieved Knowledge Ascendancy"

        if civilization.stability >= 500:
            return civilization.name + " achieved Resilient Civilization"

        if civilization.population >= 800:
            return civilization.name + " achieved Territorial Federation"

    return None
