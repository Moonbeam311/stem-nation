"""
STEM NATION PROJECT CONSTITUTION
Unified Canonical Handoff Document
"""

def show_constitution():
    print("=" * 80)
    print("STEM NATION PROJECT CONSTITUTION")
    print("=" * 80)
    print()

    print("Platform: STEM Nation Civilization Strategy Platform")
    print("Core Engine: Nation Builder Engine")
    print()

    print("PURPOSE")
    print("-" * 80)
    print("A classroom civilization simulation where students manage civilizations,")
    print("explore the world, develop knowledge, build alliances, discover artifacts,")
    print("and compete for victory.")
    print()
    print("The platform is designed as a civilization laboratory for learning history,")
    print("systems thinking, and strategy.")
    print()

    print("FOUNDATIONAL PRINCIPLE")
    print("-" * 80)
    print("The Nation Builder Engine is the core system.")
    print("All interfaces, consoles, and dashboards must call the engine,")
    print("not replicate it.")
    print()
    print("Interface Layer")
    print("    ↓")
    print("Platform Layer")
    print("    ↓")
    print("Simulation Engine")
    print()

    print("ARCHITECTURE LAYERS")
    print("-" * 80)

    print("1. SIMULATION LAYER")
    print("Controls civilization behavior and world systems.")
    print()
    print("Canonical engines:")
    engines = [
        "simulation_engine",
        "civilization_engine",
        "event_engine",
        "trait_engine",
        "diplomacy_engine",
        "exploration_engine",
        "artifact_registry",
        "map_engine",
        "chronicle_engine",
        "leaderboard_engine",
        "advisor_system",
        "library_engine",
        "dashboard_engine",
    ]
    for e in engines:
        print(" -", e)
    print()
    print("These engines contain all simulation logic.")
    print("They must never be duplicated in the interface layer.")
    print()

    print("2. PLATFORM LAYER")
    print("Controls simulation flow and classroom management.")
    print()
    platform_files = [
        "main.py",
        "session_manager.py",
        "decision_engine.py",
        "civilization_registry.py",
    ]
    for f in platform_files:
        print(" -", f)
    print()
    print("Responsibilities:")
    responsibilities = [
        "teacher console",
        "civilization selection",
        "session management",
        "student decision framework",
    ]
    for r in responsibilities:
        print(" -", r)
    print()

    print("3. INTERFACE LAYER")
    print("Displays simulation state.")
    print()
    interface_files = [
        "web_app.py",
        "templates/index.html",
        "templates/student_join.html",
        "templates/civilization_dashboard.html",
    ]
    for f in interface_files:
        print(" -", f)
    print()
    print("Responsibilities:")
    interface_responsibilities = [
        "display dashboard",
        "display map",
        "display chronicle",
        "display leaderboard",
        "allow teacher to advance turns",
    ]
    for r in interface_responsibilities:
        print(" -", r)
    print()
    print("The interface does not simulate the world.")
    print("It renders the output of the simulation engine.")
    print()

    print("CORE SIMULATION FLOW")
    print("-" * 80)
    steps = [
        "Teacher advances turn",
        "simulation_engine.run_turn()",
        "Diplomacy phase",
        "Event generation",
        "Trait bonuses applied",
        "Economic growth",
        "Territorial expansion",
        "Technology research chance",
        "Exploration attempts",
        "Artifact discovery",
        "Chronicle update",
        "Leaderboard update",
        "Victory check",
    ]
    for step in steps:
        print(" -", step)
    print()

    print("CIVILIZATION MODEL")
    print("-" * 80)
    print("Defined in: civilization_engine.py")
    print()
    civ_attrs = [
        "name",
        "population",
        "food",
        "wealth",
        "technology",
        "stability",
        "traits",
        "environment",
    ]
    for a in civ_attrs:
        print(" -", a)
    print()

    print("WORLD MAP SYSTEM")
    print("-" * 80)
    print("Defined in: map_engine.py")
    print()
    print("Regions:")
    regions = [
        "River Valley",
        "Forest Belt",
        "Highland Ridge",
        "Coastal Sea",
        "Central Basin",
        "Trade Crossroads",
        "Island Chain",
    ]
    for r in regions:
        print(" -", r)
    print()
    print("Functions:")
    map_funcs = [
        "display_map()",
        "attempt_expansion()",
        "apply_resource_bonus()",
        "get_regions()",
    ]
    for f in map_funcs:
        print(" -", f)
    print()

    print("KNOWLEDGE AND ARTIFACT SYSTEM")
    print("-" * 80)
    print("Artifacts defined in: data/artifacts.json")
    print("Managed by: artifact_registry.py, library_engine.py")
    print()
    bonuses = [
        "technology bonuses",
        "wealth bonuses",
        "stability bonuses",
    ]
    print("Artifact effects:")
    for b in bonuses:
        print(" -", b)
    print()

    print("CHRONICLE SYSTEM")
    print("-" * 80)
    print("Defined in: chronicle_engine.py")
    chronicle_records = [
        "major events",
        "alliances",
        "territorial expansion",
        "artifact discoveries",
        "historical milestones",
    ]
    for c in chronicle_records:
        print(" -", c)
    print()

    print("LEADERBOARD SYSTEM")
    print("-" * 80)
    print("Defined in: leaderboard_engine.py")
    print("Scores calculated from:")
    score_fields = [
        "population",
        "food",
        "wealth",
        "technology",
        "stability",
    ]
    for s in score_fields:
        print(" -", s)
    print()

    print("VICTORY CONDITIONS")
    print("-" * 80)
    print("Economic Dominance: wealth >= 200")
    print("Knowledge Ascendancy: technology >= 200")
    print("Resilient Civilization: stability >= 200")
    print("Territorial Federation: population >= 300")
    print()

    print("SYSTEMS THAT MUST NEVER BE REBUILT")
    print("-" * 80)
    protected = [
        "simulation_engine",
        "civilization_engine",
        "event_engine",
        "trait_engine",
        "diplomacy_engine",
        "exploration_engine",
        "artifact_registry",
        "civilization_registry",
        "library_engine",
        "dashboard_engine",
        "chronicle_engine",
        "leaderboard_engine",
        "map_engine",
        "advisor_system",
    ]
    for p in protected:
        print(" -", p)
    print()
    print("Future work must extend or call these systems, not recreate them.")
    print()

    print("CURRENT DEVELOPMENT STATE")
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
    print("Overall system status:")
    print("Engine Layer: 100%")
    print("Platform Layer: ~85%")
    print("Interface Layer: ~40%")
    print()

    print("NEXT DEVELOPMENT PHASE")
    print("-" * 80)
    next_phase = [
        "Interactive map visualization",
        "Artifact library UI",
        "Teacher dashboard panel",
        "Civilization identity themes",
        "Chronicle export system",
        "Cloud deployment",
    ]
    for item in next_phase:
        print(" -", item)
    print()
    print("These systems present the simulation, not recreate it.")
    print()

    print("DEVELOPMENT GUARDRAILS")
    print("-" * 80)
    guardrails = [
        "The simulation engine controls the world.",
        "The interface layer only displays results.",
        "New systems integrate with existing engines.",
        "Engine architecture must remain modular.",
        "The Nation Builder Engine remains the core of the platform.",
    ]
    for g in guardrails:
        print(" -", g)
    print()

    print("LONG-TERM VISION")
    print("-" * 80)
    print("STEM Nation becomes a classroom civilization laboratory where students:")
    vision = [
        "build civilizations",
        "manage resources",
        "form alliances",
        "explore unknown lands",
        "discover artifacts",
        "create historical timelines",
        "compete for victory",
    ]
    for v in vision:
        print(" -", v)
    print()
    print("The platform teaches:")
    teaches = [
        "history",
        "economics",
        "systems thinking",
        "strategy",
        "collaboration",
        "scientific reasoning",
    ]
    for t in teaches:
        print(" -", t)
    print()

    print("WHAT THIS CONSTITUTION PROTECTS")
    print("-" * 80)
    protections = [
        "months of engine work remain intact",
        "future development extends the engine instead of replacing it",
        "the project can survive multiple AI sessions without architectural drift",
    ]
    for p in protections:
        print(" -", p)
    print()

if __name__ == "__main__":
    show_constitution()
