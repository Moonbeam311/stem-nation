from map_display_engine import display_visual_map
import random


class WorldMap:

    def __init__(self):

        self.regions = []

        self.connections = {}


    def generate_regions(self, civilizations):

        environment_regions = {
            "river": ["River Valley", "Floodplain Basin"],
            "forest": ["Forest Belt", "Timber Highlands"],
            "highland": ["Highland Ridge", "Mountain Plateau"],
            "coastal": ["Coastal Sea", "Harbor Coast"],
            "steppe": ["Open Steppe", "Frontier Plains"],
            "desert": ["Desert Oasis", "Dune Basin"]
        }

        neutral_regions = [
            "Central Basin",
            "Trade Crossroads",
            "Frontier Plains",
            "Island Chain"
        ]

        used = []

        for civ in civilizations:

            env = getattr(civ, "environment", None)

            if env in environment_regions:

                region_name = random.choice(environment_regions[env])

            else:

                region_name = random.choice(neutral_regions)

            self.regions.append({
                "name": region_name,
                "owner": civ.name,
                "hidden": False
            })

            used.append(region_name)

        for region in neutral_regions:

            if region not in used:

                self.regions.append({
                    "name": region,
                    "owner": None,
                    "hidden": False
                })


        self.regions.append({
            "name": "Hy-Brasil",
            "owner": None,
            "hidden": True
        })


    def assign_starting_regions(self, civilizations):

        self.generate_regions(civilizations)


    def display_map(self, civilizations=None):

        display_visual_map(self.regions, civilizations)

        for region in self.regions:

            if region["hidden"]:
                continue

            owner = region["owner"] if region["owner"] else "Unclaimed"

            print(f"{region['name']} — {owner}")


    def apply_resource_bonus(self, civ):

        pass


    def attempt_expansion(self, civ):

        unclaimed = [r for r in self.regions if r["owner"] is None and not r["hidden"]]

        if not unclaimed:
            return

        if random.random() < 0.2:

            region = random.choice(unclaimed)

            region["owner"] = civ.name

            print(f"{civ.name} expanded into {region['name']}")


    def get_regions(self):

        return self.regions

# ------------------------------------------------
# AUT0MAN MAP COMPATIBILITY
# ------------------------------------------------

def generate_world_map():
    """
    Simple world map generator used by the web interface.
    """

    regions = [
        {"name": "River Valley", "terrain": "river", "owner": None},
        {"name": "Forest Belt", "terrain": "forest", "owner": None},
        {"name": "Highland Ridge", "terrain": "mountain", "owner": None},
        {"name": "Coastal Sea", "terrain": "coast", "owner": None},
        {"name": "Central Basin", "terrain": "plains", "owner": None},
        {"name": "Trade Crossroads", "terrain": "plains", "owner": None},
        {"name": "Island Chain", "terrain": "islands", "owner": None},
    ]

    return regions



# ------------------------------------------------
# REGION ADJACENCY (MAP LOGIC)
# ------------------------------------------------

NEIGHBOR_MAP = {
    "River Valley": ["Forest Belt", "Central Basin"],
    "Forest Belt": ["River Valley", "Highland Ridge"],
    "Highland Ridge": ["Forest Belt", "Central Basin"],
    "Coastal Sea": ["Central Basin", "Island Chain"],
    "Central Basin": ["River Valley", "Highland Ridge", "Coastal Sea", "Trade Crossroads"],
    "Trade Crossroads": ["Central Basin", "Island Chain"],
    "Island Chain": ["Trade Crossroads", "Coastal Sea"]
}

def get_neighbors(region_name):
    return NEIGHBOR_MAP.get(region_name, [])
