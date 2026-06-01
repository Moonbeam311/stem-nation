import asyncio
from pathlib import Path
import edge_tts

VOICE = "en-US-JennyNeural"

# STEM_NATION_INTRO_AUDIO_REGEN_V1
scripts = {
    "intro1_demo.mp3": (
        "Every nation begins with a decision."
    ),
    "intro5_demo.mp3": (
        "Before a nation can lead, it must learn to think clearly. "
        "Give clear instructions. Test the process. Revise what fails."
    ),
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
        "Carry this forward. What you observe will shape what you choose."
    ),
    "academy_decision_demo.mp3": (
        "You have observed the land. "
        "You have answered the first questions. "
        "You have studied advantage, risk, and possibility. "
        "Now observation becomes action. "
        "The strategic map will ask your civilization to choose where it begins. "
        "Every settlement decision carries consequence. "
        "Enter the map prepared to defend your choice with evidence from the land."
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
