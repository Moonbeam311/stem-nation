def initialize_library(civ, starter_knowledge=None):

    civ.library = {
        "inherited": starter_knowledge if starter_knowledge else [],
        "artifacts": [],
        "shared": []
    }


def add_artifact(civ, artifact_name):

    if artifact_name not in civ.library["artifacts"]:
        civ.library["artifacts"].append(artifact_name)


def share_knowledge(source_civ, target_civ, knowledge):

    if knowledge not in target_civ.library["shared"]:
        target_civ.library["shared"].append(f"{knowledge} (from {source_civ.name})")


def display_library(civ):

    print(f"\n===== {civ.name.upper()} LIBRARY =====")

    print("\nInherited Knowledge")
    for item in civ.library["inherited"]:
        print(f"• {item}")

    print("\nArtifacts")
    for item in civ.library["artifacts"]:
        print(f"• {item}")

    print("\nShared Knowledge")
    for item in civ.library["shared"]:
        print(f"• {item}")
