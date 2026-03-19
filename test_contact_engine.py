import world_state_engine as world
import contact_engine

civilizations = [
    {
        "name": "River Alliance",
        "capital": {"x": 10, "y": 10},
        "influence": 15
    },
    {
        "name": "Forest League",
        "capital": {"x": 18, "y": 14},
        "influence": 12
    },
    {
        "name": "Highland Order",
        "capital": {"x": 80, "y": 80},
        "influence": 10
    }
]

world.advance_turn()
contact_engine.detect_contacts(civilizations)

print("TURN:", world.get_world_state()["turn"])
print("CONTACT STAGES:", world.get_world_state()["contact_stages"])
print("CHRONICLE:", world.get_world_state()["chronicle"])
