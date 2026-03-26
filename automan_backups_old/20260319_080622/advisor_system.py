
# ------------------------------------------------
# ADVISOR SYSTEM V2 — CONTEXT-AWARE
# ------------------------------------------------

def advisor_response(civilization, context=None):

    name = getattr(civilization, "name", "Civilization")

    population = getattr(civilization, "population", 0)
    food = getattr(civilization, "food", 0)
    wealth = getattr(civilization, "wealth", 0)
    technology = getattr(civilization, "technology", 0)
    stability = getattr(civilization, "stability", 0)
    influence = getattr(civilization, "influence", 0)

    messages = []

    # FOOD ADVISOR
    if food < 20:
        messages.append(f"{name}: Food levels are low. Prioritize agriculture or trade.")
    
    # STABILITY ADVISOR
    if stability < 40:
        messages.append(f"{name}: Internal unrest is rising. Strengthen governance.")

    # ECONOMIC ADVISOR
    if wealth < 30:
        messages.append(f"{name}: Wealth is limited. Expand trade routes.")

    # TECHNOLOGY ADVISOR
    if technology < 30:
        messages.append(f"{name}: Invest in knowledge and innovation.")

    # EXPANSION / POWER ADVISOR
    if influence > 70:
        messages.append(f"{name}: Your influence is growing. Expansion opportunities available.")

    # BALANCED STATE
    if not messages:
        messages.append(f"{name}: Civilization is stable. Maintain balanced growth.")

    return {
        "advisor": "Council",
        "messages": messages
    }


def generate_advice(civilization):

    response = advisor_response(civilization)

    return response["messages"]


def show_advisor_council():
    return [
        "Strategic Advisor",
        "Economic Advisor",
        "Diplomatic Advisor",
        "Exploration Advisor"
    ]
