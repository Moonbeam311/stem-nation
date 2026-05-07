import asyncio
from pathlib import Path
import edge_tts

VOICE = "en-US-JennyNeural"

scripts = {
    "academy_individual_demo.mp3": (
        "Every civilization begins with observation. "
        "Before there is a government, before there is a city, before there is a nation, "
        "there is a person studying the land. "
        "The quality of what follows depends on how that person thinks. "
        "Begin your First Observation Notes. What did the land reveal before you made a decision?"
    ),
    "academy_role_demo.mp3": (
        "An individual does not observe in isolation. "
        "Every decision reaches beyond the person who makes it. "
        "A river can feed a people. A mountain can protect them. "
        "A poor choice of land can weaken everything that follows. "
        "This is the beginning of responsibility. "
        "Prepare your Terrain Analysis Report. Which land feature creates the greatest advantage, and which creates the greatest risk?"
    ),
    "academy_decision_demo.mp3": (
        "You have observed the land. "
        "You have studied its strengths. "
        "You have considered its risks. "
        "Now your people need a place to begin. "
        "Every settlement decision carries consequence. "
        "Where will your people settle first, and what evidence supports your choice? "
        "Begin your Settlement Recommendation Portfolio. Identify the region, explain the advantage, name the risk, and defend the decision."
    ),
}

async def main():
    out_dir = Path("static")
    out_dir.mkdir(exist_ok=True)

    for filename, text in scripts.items():
        path = out_dir / filename
        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE,
            rate="+7%",
            volume="+0%"
        )
        await communicate.save(str(path))
        print(f"CREATED: {path}")

asyncio.run(main())
