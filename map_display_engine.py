def display_visual_map(regions, civilizations):

    print("\n================ WORLD MAP ================\n")

    civ_symbols = {c.name: getattr(c, "symbol", "?") for c in civilizations}
    civ_colors = {c.name: getattr(c, "color", "Neutral") for c in civilizations}

    visible = [r for r in regions if not r.get("hidden")]

    for r in visible:

        owner = r.get("owner") if r.get("owner") else "Unclaimed"

        if owner == "Unclaimed":
            print(f"[{r['name']}: Unclaimed]")
        else:
            symbol = civ_symbols.get(owner, "?")
            color = civ_colors.get(owner, "Neutral")
            print(f"[{r['name']} {symbol} {owner}] ({color})")

    print("\n==========================================\n")
