from dataclasses import dataclass, asdict
import json
from pathlib import Path

def includes_any(text, words):
    return any(word in text for word in words)

def analyze(text):
    t = text.lower()
    return {
        "everything": includes_any(t, ["everything", "all the items", "all items", "all supplies", "stuff"]),
        "backpack": includes_any(t, ["backpack", "bag", "bookbag"]),
        "open": includes_any(t, ["open", "unzip", "open the backpack", "open backpack", "open the bag", "open bag"]),
        "put": includes_any(t, ["put", "place", "pack", "load", "insert"]),
        "papers": includes_any(t, ["paper", "papers", "folder", "notebook", "flat"]),
        "flat": includes_any(t, ["flat", "against the back", "against back", "first"]),
        "heavy": includes_any(t, ["heavy", "bottom", "first"]),
        "bottle": includes_any(t, ["water", "bottle"]),
        "closed": includes_any(t, ["closed", "close", "cap", "lid", "tight", "sealed"]),
        "lunch": includes_any(t, ["lunch", "lunchbox", "food"]),
        "upright": includes_any(t, ["upright", "right side up", "standing"]),
        "pencil": includes_any(t, ["pencil"]) or __import__("re").search(r"\\bpen\\b", t) is not None,
        "tablet": includes_any(t, ["tablet", "computer", "device", "laptop"]),
        "zip": includes_any(t, ["zip", "zipper", "close the backpack", "close bag", "close the bag"]),
    }

def fresh_state():
    return {
        "backpackOpen": False,
        "dumpedEverything": False,
        "papersFlat": False,
        "bottleClosed": False,
        "bottlePacked": False,
        "lunchUpright": False,
        "lunchPacked": False,
        "pencilPacked": False,
        "tabletPacked": False,
        "zipped": False,
        "spill": False,
        "crushedPapers": False,
        "cannotClose": False,
        "warning": "",
    }

def process_instruction(raw, state):
    result = analyze(raw)
    messages = []

    # Expected final rule: open bag/backpack opens only.
    if result["open"] and result["backpack"] and not result["put"]:
        state["backpackOpen"] = True
        state["warning"] = ""
        messages.append("I opened the backpack.")
        messages.append("Good first step. Now ask: what item should go in first, and what condition matters?")
        return messages

    # Pack everything creates mess.
    if result["everything"] and result["backpack"] and result["put"]:
        state["dumpedEverything"] = True
        state["spill"] = True
        state["crushedPapers"] = True
        state["cannotClose"] = True
        state["warning"] = "Everything was dumped together."
        messages.append("I dumped everything into the backpack because the instruction did not tell me order, placement, or conditions.")

    if result["papers"] and result["backpack"] and result["put"] and result["flat"]:
        state["papersFlat"] = True
        state["crushedPapers"] = False
        messages.append("I placed the notebook and folder flat against the back of the backpack.")
    elif result["papers"] and result["backpack"] and result["put"] and not result["flat"]:
        state["crushedPapers"] = True
        messages.append("I put the papers in, but they bent because the instruction did not say to keep them flat.")

    if result["bottle"] and result["closed"]:
        state["bottleClosed"] = True
        messages.append("I closed the water bottle tightly.")

    if result["bottle"] and result["backpack"] and result["put"]:
        state["bottlePacked"] = True
        if not state["bottleClosed"]:
            state["spill"] = True
            state["warning"] = "The bottle was packed without being closed first."
            messages.append("I packed the water bottle, but it spilled because the instruction did not say to close it first.")
        else:
            messages.append("I packed the closed water bottle.")

    if result["lunch"] and result["upright"]:
        state["lunchUpright"] = True
        messages.append("I kept the lunchbox upright.")

    if result["lunch"] and result["backpack"] and result["put"]:
        state["lunchPacked"] = True
        if not state["lunchUpright"]:
            messages.append("I packed the lunchbox, but the instruction did not say to keep it upright.")
        else:
            messages.append("I packed the lunchbox upright.")

    if result["pencil"] and result["backpack"] and result["put"]:
        state["pencilPacked"] = True
        messages.append("I packed the pencil.")

    if result["tablet"] and result["backpack"] and result["put"]:
        state["tabletPacked"] = True
        messages.append("I packed the tablet.")

    if result["zip"]:
        if state["spill"] or state["crushedPapers"] or state["dumpedEverything"]:
            state["cannotClose"] = True
            messages.append("I tried to zip the backpack, but the messy packing made it hard to close.")
        else:
            state["zipped"] = True
            state["cannotClose"] = False
            messages.append("I zipped the backpack closed.")

    if not messages:
        messages.append("I heard words, but the step was not clear enough for me to pack anything yet.")
        messages.append("Try naming the item, action, condition, and location.")

    return messages

@dataclass
class Case:
    instruction: str
    expect: dict
    note: str

cases = [
    Case("open the backpack", {"backpackOpen": True, "pencilPacked": False, "tabletPacked": False}, "Open should not pack anything."),
    Case("open the bag", {"backpackOpen": True, "pencilPacked": False, "tabletPacked": False}, "Bag should be recognized as backpack."),
    Case("unzip the bag", {"backpackOpen": True, "pencilPacked": False}, "Unzip should open only."),
    Case("pack the backpack", {"pencilPacked": False, "tabletPacked": False, "dumpedEverything": False}, "Too general; should ask for item/action/location/condition."),
    Case("put everything in the backpack", {"dumpedEverything": True, "spill": True, "crushedPapers": True}, "Starter mistake."),
    Case("put the pencil in the backpack", {"pencilPacked": True}, "Pencil should pack only when named."),
    Case("put the pen in the bag", {"pencilPacked": True}, "Pen synonym should pack pencil."),
    Case("put the tablet in the backpack", {"tabletPacked": True}, "Tablet packs, but may need future protected/closed distinction."),
    Case("put the closed tablet in the backpack", {"tabletPacked": True}, "Closed tablet should pack; future visual should show protected/closed."),
    Case("put the water bottle in the backpack", {"bottlePacked": True, "spill": True}, "Bottle spills if not closed first."),
    Case("close the water bottle", {"bottleClosed": True}, "Close bottle only."),
    Case("put the closed water bottle in the backpack", {"bottleClosed": True, "bottlePacked": True, "spill": False}, "Closed bottle should not spill."),
    Case("put the lunchbox in the backpack", {"lunchPacked": True}, "Lunch packs, but without upright condition."),
    Case("keep the lunchbox upright", {"lunchUpright": True}, "Condition only."),
    Case("put the lunchbox upright in the backpack", {"lunchPacked": True, "lunchUpright": True}, "Lunch should pack upright."),
    Case("put the notebook and folder flat against the back of the backpack", {"papersFlat": True, "crushedPapers": False}, "Papers should be protected."),
    Case("put the papers in the backpack", {"crushedPapers": True}, "Papers bend without flat condition."),
    Case("zip the backpack", {"zipped": True}, "Zip should close if no mess."),
]

results = []
for case in cases:
    state = fresh_state()
    messages = process_instruction(case.instruction, state)
    failures = []
    for key, expected_value in case.expect.items():
        actual = state.get(key)
        if actual != expected_value:
            failures.append(f"{key}: expected {expected_value}, got {actual}")
    results.append({
        "instruction": case.instruction,
        "messages": messages,
        "state": state,
        "expected": case.expect,
        "pass": not failures,
        "failures": failures,
        "note": case.note,
    })

print("=== BACKPACK LAB BEHAVIOR AUDIT ===")
for r in results:
    status = "PASS" if r["pass"] else "FAIL"
    print(f"\n[{status}] {r['instruction']}")
    print("Messages:", " | ".join(r["messages"]))
    if r["failures"]:
        print("Failures:", "; ".join(r["failures"]))

Path("stem-nation/BACKPACK_BEHAVIOR_AUDIT_RESULTS.json").write_text(
    json.dumps(results, indent=2),
    encoding="utf-8"
)
print("\nWROTE: stem-nation/BACKPACK_BEHAVIOR_AUDIT_RESULTS.json")
