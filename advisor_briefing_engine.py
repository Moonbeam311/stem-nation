
# ------------------------------------------------
# Advisor Briefing Engine
# ------------------------------------------------

import advisor_system
import world_state_engine as world


def generate_turn_briefing():

    state = world.get_world_state()
    civilizations = state.get("civilizations", {})

    report = []
    report.append("\n==============================")
    report.append(" ADVISOR COUNCIL BRIEFING")
    report.append("==============================")

    for civ in civilizations.values():

        name = civ.get("name","Civilization")

        report.append(f"\n{name}")

        advice = advisor_system.generate_advice(civ)

        for entry in advice:
            report.append(f"{entry['advisor']}: {entry['message']}")

    return "\n".join(report)
