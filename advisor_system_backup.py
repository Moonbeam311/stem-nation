# ------------------------------------------------
# Advisor System
# ------------------------------------------------

def generate_advice(*args):
    """
    Compatibility function supporting multiple call patterns.
    """

    if len(args) == 1:
        civilization = args[0]
        event = None
    elif len(args) == 2:
        event, civilization = args
    else:
        return ["Advisor system received invalid parameters."]

    name = getattr(civilization, "name", "Civilization")

    advice = []

    advice.append(f"The council advises {name} to maintain stability.")
    advice.append("Invest in knowledge and trade when possible.")
    advice.append("Watch alliances carefully.")

    return advice


def advisor_response(civilization, context=None):
    '''
    Basic advisor response generator.
    This placeholder prevents import errors and can be upgraded later.
    '''
    return {
        "advisor": "Strategic Council",
        "message": "The council recommends balanced development across food, stability, and knowledge."
    }


def show_advisor_council():
    '''
    Displays advisor council members.
    '''
    council = [
        "Strategic Advisor",
        "Economic Advisor",
        "Diplomatic Advisor",
        "Exploration Advisor"
    ]

    return council
