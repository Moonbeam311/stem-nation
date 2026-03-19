from pathlib import Path

path = Path("main.py")
text = path.read_text(encoding="utf-8", errors="replace")

SYMBOL_MAP = """
SYMBOL_MAP = {
    "Mississippian": "^",
    "Susquehannock": "T",
    "Inca": "*",
    "Phoenician": "~"
}
"""

if "SYMBOL_MAP =" not in text:
    text = SYMBOL_MAP + "\n" + text

text = text.replace(
    'print(f"{i}. {symbol} {name} — {motto}")',
    'print(f"{i}. {SYMBOL_MAP.get(name, "?")} {name} — {motto}")'
)

text = text.replace(
    'print(f"{i}. {civ[\'symbol\']} {civ[\'name\']} — {civ[\'motto\']}")',
    'print(f"{i}. {SYMBOL_MAP.get(civ[\'name\'], "?")} {civ[\'name\']} — {civ[\'motto\']}")'
)

path.write_text(text, encoding="utf-8")
print("Atlas symbol patch applied.")
