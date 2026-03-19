"""
CHRONICLE EXPORTER
Exports civilization history for classroom artifacts
"""

import json


def export_chronicle(chronicle, filename="chronicle_export.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(chronicle, f, indent=4)

    print("Chronicle exported:", filename)
