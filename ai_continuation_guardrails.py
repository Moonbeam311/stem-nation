"""
AI CONTINUATION GUARDRAILS
STEM Nation Civilization Strategy Platform

Purpose:
Ensure any future AI session continues development without
rebuilding or damaging the Nation Builder Engine architecture.
"""

def show_guardrails():

    print("=" * 80)
    print("STEM NATION AI CONTINUATION GUARDRAILS")
    print("=" * 80)
    print()

    print("PROJECT IDENTITY")
    print("-" * 80)
    print("Platform: STEM Nation Civilization Strategy Platform")
    print("Core Engine: Nation Builder Engine")
    print()

    print("PRIMARY RULE")
    print("-" * 80)
    print("The Nation Builder Engine already exists.")
    print("Future development must EXTEND it, not rebuild it.")
    print()

    print("ENGINE SYSTEMS (DO NOT REBUILD)")
    print("-" * 80)

    engines = [
        "simulation_engine.py",
        "civilization_engine.py",
        "event_engine.py",
        "trait_engine.py",
        "diplomacy_engine.py",
        "exploration_engine.py",
        "artifact_registry.py",
        "civilization_registry.py",
        "library_engine.py",
        "dashboard_engine.py",
        "chronicle_engine.py",
        "leaderboard_engine.py",
        "map_engine.py",
        "advisor_system.py"
    ]

    for e in engines:
        print("PROTECTED ENGINE:", e)

    print()

    print("ARCHITECTURE STRUCTURE")
    print("-" * 80)

    print("Interface Layer")
    print("   web_app.py")
    print("   HTML templates")
    print("       ↓")
    print("Platform Layer")
    print("   main.py")
    print("   session_manager.py")
    print("   decision_engine.py")
    print("       ↓")
    print("Simulation Layer")
    print("   simulation_engine.py")
    print("       ↓")
    print("Subsystem Engines")
    print()

    print("CORRECT TURN FLOW")
    print("-" * 80)

    steps = [
        "Teacher advances turn",
        "web_app calls simulation_engine.run_turn()",
        "simulation_engine executes diplomacy phase",
        "event_engine generates world events",
        "trait_engine applies bonuses",
        "map_engine processes expansion",
        "exploration_engine attempts discoveries",
        "artifact_registry resolves artifacts",
        "chronicle_engine records history",
        "leaderboard_engine updates rankings"
    ]

    for step in steps:
        print(" -", step)

    print()

    print("INTERFACE RESPONSIBILITIES")
    print("-" * 80)

    ui_tasks = [
        "Render dashboard",
        "Display world map",
        "Display chronicle",
        "Display leaderboard",
        "Allow teacher to advance turns"
    ]

    for task in ui_tasks:
        print(" -", task)

    print()

    print("INTERFACE MUST NOT")
    print("-" * 80)

    forbidden = [
        "implement diplomacy logic",
        "implement event systems",
        "implement exploration logic",
        "implement artifact logic",
        "implement victory systems",
        "duplicate simulation mechanics"
    ]

    for rule in forbidden:
        print("DO NOT:", rule)

    print()

    print("CURRENT PROJECT STATUS")
    print("-" * 80)

    print("Simulation Engine: COMPLETE")
    print("Civilization Systems: COMPLETE")
    print("Artifact System: COMPLETE")
    print("Exploration System: COMPLETE")
    print("Diplomacy System: COMPLETE")
    print("Chronicle System: COMPLETE")
    print("Leaderboard System: COMPLETE")
    print("Teacher Console: OPERATIONAL")
    print()

    print("DEVELOPMENT PRIORITY")
    print("-" * 80)

    next_phase = [
        "Interactive map visualization",
        "Artifact library interface",
        "Teacher dashboard UI",
        "Civilization identity themes",
        "Chronicle export system",
        "Cloud deployment"
    ]

    for item in next_phase:
        print("NEXT:", item)

    print()

    print("LONG TERM GOAL")
    print("-" * 80)

    print("STEM Nation becomes a classroom civilization laboratory")
    print("where students manage civilizations, explore the world,")
    print("discover knowledge, and build historical timelines.")
    print()

    print("=" * 80)
    print("END OF AI GUARDRAILS")
    print("=" * 80)


if __name__ == "__main__":
    show_guardrails()
