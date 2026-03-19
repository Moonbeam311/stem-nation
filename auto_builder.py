"""
AUTOMAN EXECUTION ENGINE
STEM Nation / Nation Builder Platform

Purpose
-------
Deterministic autonomous build assistant that extends the project
while respecting AUTOMAN governance rules.

Capabilities
------------
- Detect project structure
- Verify protected engines
- Identify missing extension modules
- Generate approved architecture extensions
- Never overwrite protected engines
"""

import os
from pathlib import Path


# ============================================================================
# AUTOMAN RULES
# ============================================================================

PROTECTED_ENGINES = [
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
    "advisor_system.py",
    "population_engine.py",
    "food_system.py",
    "construction_engine.py",
]

PROJECT_ROOT = Path(".")


# ============================================================================
# SAFETY CHECKS
# ============================================================================

def check_protected_engines():
    print("\nChecking protected engines...\n")
    missing = []

    for engine in PROTECTED_ENGINES:
        if not (PROJECT_ROOT / engine).exists():
            missing.append(engine)

    if missing:
        print("WARNING: Missing protected engines:")
        for m in missing:
            print(" -", m)
    else:
        print("All protected engines present.")


# ============================================================================
# EXTENSION GENERATION
# ============================================================================

def create_turn_controller():
    file = PROJECT_ROOT / "turn_controller.py"

    if file.exists():
        print("turn_controller.py already exists.")
        return

    code = '''"""
TURN CONTROLLER
Authoritative turn coordination layer for Nation Builder
"""

from simulation_engine import run_turn
from leaderboard_engine import update_leaderboard
from victory_engine import check_victory


def execute_turn(civilizations, decisions):
    """
    Centralized turn resolution
    """

    result = run_turn(civilizations, decisions)
    update_leaderboard(civilizations)
    victory = check_victory(civilizations)

    return {
        "civilizations": civilizations,
        "result": result,
        "victory": victory
    }
'''
    file.write_text(code, encoding="utf-8")
    print("Created turn_controller.py")


def create_decision_router():
    file = PROJECT_ROOT / "decision_router.py"

    if file.exists():
        print("decision_router.py already exists.")
        return

    code = '''"""
DECISION ROUTER
Maps classroom decisions into simulation inputs
"""

def route_decision(decision, civ):
    if decision == "agriculture":
        civ["food"] = civ.get("food", 0) + 10

    elif decision == "trade":
        civ["wealth"] = civ.get("wealth", 0) + 10

    elif decision == "research":
        civ["technology"] = civ.get("technology", 0) + 10

    elif decision == "infrastructure":
        civ["construction"] = civ.get("construction", 0) + 5

    elif decision == "stability":
        civ["stability"] = civ.get("stability", 0) + 5

    return civ
'''
    file.write_text(code, encoding="utf-8")
    print("Created decision_router.py")


def create_chronicle_exporter():
    file = PROJECT_ROOT / "chronicle_exporter.py"

    if file.exists():
        print("chronicle_exporter.py already exists.")
        return

    code = '''"""
CHRONICLE EXPORTER
Exports civilization history for classroom artifacts
"""

import json


def export_chronicle(chronicle, filename="chronicle_export.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(chronicle, f, indent=4)

    print("Chronicle exported:", filename)
'''
    file.write_text(code, encoding="utf-8")
    print("Created chronicle_exporter.py")


# ============================================================================
# PROJECT SCAN
# ============================================================================

def scan_project():
    print("\nScanning project structure...\n")

    for root, dirs, files in os.walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in {"__pycache__", ".git", ".venv", "venv"}]
        for file in files:
            if file.endswith(".py"):
                print(os.path.join(root, file))


# ============================================================================
# BUILD PLAN
# ============================================================================

def execute_automan():
    print("\n==============================")
    print("AUTOMAN BUILD EXECUTION")
    print("==============================\n")

    scan_project()
    check_protected_engines()

    print("\nGenerating approved extensions...\n")

    create_turn_controller()
    create_decision_router()
    create_chronicle_exporter()

    print("\nAUTOMAN COMPLETE")
    print("Platform safely extended without modifying core engines.")


# ============================================================================
# ENTRY
# ============================================================================

if __name__ == "__main__":
    execute_automan()
