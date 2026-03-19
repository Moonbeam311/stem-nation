import random
from event_engine import generate_event
from advisor_system import advisor_response, show_advisor_council
from diplomacy_engine import attempt_diplomacy, apply_alliance_bonuses
from trait_engine import apply_environment_bonus, apply_trait_bonus
from exploration_engine import attempt_exploration


technologies = [
    "Agriculture",
    "Navigation",
    "Engineering",
    "Diplomatic Protocol",
    "Academy Systems"
]


def apply_technology_bonus(civ, tech):

    if tech == "Agriculture":
        civ.food += 15

    elif tech == "Navigation":
        civ.wealth += 15

    elif tech == "Engineering":
        civ.wealth += 10
        civ.technology += 5

    elif tech == "Diplomatic Protocol":
        civ.stability += 10

    elif tech == "Academy Systems":
        civ.technology += 15


def run_turn(turn, civilizations, world):

    print(f"\n================ TURN {turn} ================")

    # diplomacy phase
    attempt_diplomacy(civilizations)

    for civ in civilizations:

        print(f"\n--- {civ.name} ---")

        event = generate_event()

        print(f"Event: {event}")

        advice = advisor_response(event)

        print(f"Primary Advisor says: {advice}")

        show_advisor_council(event)

        civ.apply_event(event)

        world.apply_resource_bonus(civ)

        world.attempt_expansion(civ)

        if random.random() < 0.25:

            tech = random.choice(technologies)

            print(f"{civ.name} researches {tech}")

            apply_technology_bonus(civ, tech)

        if random.random() < 0.20:

            civ.wealth += 10

            print(f"{civ.name} expands economic infrastructure")

        print("\nUpdated Civilization Stats:")

        civ.display_stats()

    # alliance bonuses
    apply_alliance_bonuses(civilizations)

    # exploration phase
    attempt_exploration(civilizations, world.get_regions())