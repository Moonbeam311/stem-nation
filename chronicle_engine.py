chronicle = []


def record_event(turn, text):

    entry = f"Turn {turn} - {text}"

    chronicle.append(entry)

    print(f"\n[Chronicle] {entry}")


def show_chronicle():

    print("\n===== WORLD CHRONICLE =====")

    for entry in chronicle:

        print(entry)
