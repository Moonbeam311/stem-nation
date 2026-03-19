def display_dashboard(civ):

    symbol = getattr(civ, "symbol", "?")
    color = getattr(civ, "color", "Neutral")
    env = getattr(civ, "environment", "Unknown")
    traits = getattr(civ, "traits", [])

    print(f"\n===== {symbol} {civ.name.upper()} CIVILIZATION =====")

    print("\nPopulation:", civ.population)
    print("Food:", civ.food)
    print("Wealth:", civ.wealth)
    print("Technology:", civ.technology)
    print("Stability:", civ.stability)

    print("\nEnvironment:", env)
    print("Color:", color)

    print("\nTraits")
    for t in traits:
        print(f"• {t}")

    if hasattr(civ, "library"):

        print("\nArtifacts")
        for a in civ.library.get("artifacts", []):
            print(f"• {a}")

        print("\nKnowledge")
        for k in civ.library.get("inherited", []):
            print(f"• {k}")

        print("\nShared Knowledge")
        for s in civ.library.get("shared", []):
            print(f"• {s}")
