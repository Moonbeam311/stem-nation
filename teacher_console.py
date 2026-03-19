
"""
TEACHER COMMAND CONSOLE
Controls simulation and displays reports
"""

import world_state_engine as world
import influence_engine
import contact_engine
import trade_engine
import conflict_engine
import advisor_briefing_engine
import chronicle_viewer


def run_turn():

    state = world.get_world_state()
    civilizations = list(state.get("civilizations", {}).values())

    world.advance_turn()

    influence_engine.apply_influence(civilizations)
    contact_engine.detect_contacts(civilizations)
    trade_engine.evaluate_trade(civilizations)
    conflict_engine.evaluate_conflicts(civilizations)

    world.save_world_state()

    print("\n--- TURN COMPLETE ---")


def show_advisors():
    print(advisor_briefing_engine.generate_turn_briefing())


def show_chronicle():
    chronicle_viewer.display_chronicle()


def auto_run(turns=5):

    for i in range(turns):
        run_turn()

    print(f"\nAuto-run completed ({turns} turns)")


def teacher_console():

    while True:

        print("\n=== STEM NATION TEACHER CONSOLE ===")
        print("1. Run Turn")
        print("2. Auto Run (5 turns)")
        print("3. View Chronicle")
        print("4. Advisor Briefing")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            run_turn()

        elif choice == "2":
            auto_run()

        elif choice == "3":
            show_chronicle()

        elif choice == "4":
            show_advisors()

        elif choice == "5":
            break

        else:
            print("Invalid option")
