import re

with open("main.py","r") as f:
    text = f.read()

start = text.find("while True:")
end = text.find('print("Invalid command.")') + len('print("Invalid command.")')

new_block = """
    while True:

        print("\\nTeacher Options")
        print("1 — Advance Turn")
        print("2 — Inject Event")
        print("3 — View Map")
        print("4 — View Leaderboard")
        print("5 — View Chronicle")
        print("6 — End Simulation")

        choice = input("\\nEnter command: ")

        if choice == "1":

            run_turn(turn, civilizations, world)
            show_leaderboard(civilizations)
            turn += 1

        elif choice == "2":

            inject_event(civilizations)

        elif choice == "3":

            world.display_map()

        elif choice == "4":

            show_leaderboard(civilizations)

        elif choice == "5":

            show_chronicle()

        elif choice == "6":

            print("\\nSimulation ended.")
            break

        else:

            print("Invalid command.")
"""

fixed = text[:start] + new_block + text[end:]

with open("main.py","w") as f:
    f.write(fixed)

print("Menu repaired successfully.")
