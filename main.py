
SYMBOL_MAP = {
    "Mississippian": "^",
    "Susquehannock": "T",
    "Inca": "*",
    "Phoenician": "~"
}

# -*- coding: utf-8 -*-
import sys; sys.stdout.reconfigure(encoding="utf-8"); sys.stdin.reconfigure(encoding="utf-8")
# -*- coding: utf-8 -*-

import sys
import os

sys.stdout.reconfigure(encoding="utf-8")
sys.stdin.reconfigure(encoding="utf-8")
from civilization_engine import Civilization
from simulation_engine import run_turn
from map_engine import WorldMap
from civilization_registry import load_civilizations
from chronicle_engine import show_chronicle
from library_engine import display_library, initialize_library
from dashboard_engine import display_dashboard


def select_civilizations():

    civ_data = load_civilizations()

    print("\n===== CIVILIZATION ATLAS =====")

    for i, civ in enumerate(civ_data, start=1):
        symbol = civ.get("symbol", "?")
        motto = civ.get("motto", "")
        print(f"{i}. {symbol} {civ['name']} — {motto}")

    selected_records = []

    while len(selected_records) < 4:

        choice = input(f"\nSelect civilization {len(selected_records)+1}: ")

        if not choice.isdigit():
            print("Invalid selection")
            continue

        index = int(choice) - 1

        if index < 0 or index >= len(civ_data):
            print("Invalid selection")
            continue

        record = civ_data[index]

        if record["name"] in [r["name"] for r in selected_records]:
            print("Already selected")
            continue

        selected_records.append(record)

    civilizations = []

    for record in selected_records:

        civ = Civilization(record["name"])
        civ.environment = record.get("environment", "unknown")
        civ.traits = record.get("traits", [])
        civ.color = record.get("color", "Neutral")
        civ.symbol = record.get("symbol", "?")
        civ.banner = record.get("banner", "")
        civ.motto = record.get("motto", "")
        civ.starter_knowledge = record.get("starter_knowledge", [])

        initialize_library(civ, civ.starter_knowledge)

        civilizations.append(civ)

    return civilizations


def show_leaderboard(civilizations):

    print("\n----- LEADERBOARD -----")

    leaderboard = []

    for civ in civilizations:
        score = civ.calculate_score()
        leaderboard.append((civ.name, score, getattr(civ, "symbol", "?")))

    leaderboard.sort(key=lambda x: x[1], reverse=True)

    for rank, (name, score, symbol) in enumerate(leaderboard, start=1):
        print(f"{rank}. {symbol} {name} — {score}")


def teacher_console():

    civilizations = select_civilizations()

    world = WorldMap()
    world.assign_starting_regions(civilizations)

    turn = 1

    print("\n===== STEM NATION TEACHER COMMAND CENTER =====")

    world.display_map(civilizations)

    while True:

        print("\nTeacher Options")
        print("1 - Advance Turn")
        print("2 - View Map")
        print("3 - View Leaderboard")
        print("4 - View Chronicle")
        print("5 - End Simulation")
        print("6 - View Civilization Library")
        print("7 - View Civilization Dashboard")

        choice = input("\nEnter command: ")

        if choice == "1":

            run_turn(turn, civilizations, world)
            show_leaderboard(civilizations)
            turn += 1

        elif choice == "2":

            world.display_map(civilizations)

        elif choice == "3":

            show_leaderboard(civilizations)

        elif choice == "4":

            show_chronicle()

        elif choice == "5":

            print("\nSimulation ended.")
            break

        elif choice == "6":

            for civ in civilizations:
                display_library(civ)

        elif choice == "7":

            for civ in civilizations:
                display_dashboard(civ)

        else:

            print("Invalid command.")


if __name__ == "__main__":

    teacher_console()
