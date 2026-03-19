# ADVISOR SYSTEM V2

def generate_advice(civilization):
    name = getattr(civilization, "name", "Civilization")
    population = getattr(civilization, "population", 0)
    food = getattr(civilization, "food", 0)
    wealth = getattr(civilization, "wealth", 0)
    technology = getattr(civilization, "technology", 0)
    stability = getattr(civilization, "stability", 0)
    influence = getattr(civilization, "influence", 0)

    messages = []

    if food < 50:
        messages.append(f"{name}: Food levels are low. Prioritize agriculture or trade.")
    if wealth < 40:
        messages.append(f"{name}: Wealth is limited. Strengthen trade and production.")
    if technology < 35:
        messages.append(f"{name}: Knowledge development is lagging. Invest in research.")
    if stability < 50:
        messages.append(f"{name}: Stability is weakening. Build and govern carefully.")
    if influence > 70:
        messages.append(f"{name}: Influence is rising. Expansion opportunities are opening.")

    if not messages:
        messages.append(f"{name}: Civilization is stable. Maintain balanced growth.")

    return messages

def show_advisor_council():
    return [
        "Strategic Advisor",
        "Economic Advisor",
        "Diplomatic Advisor",
        "Exploration Advisor",
    ]
