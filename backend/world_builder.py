from config import groq_client, MODEL_NAME

def build_world_from_prompt(prompt: str):
    system_prompt = f"""
You are generating a structured game world.

Follow this EXACT format.
Do NOT add extra text.
Do NOT add numbering.

WORLD NAME: <short world name>
DESCRIPTION: <2-3 sentence description>
LOCATIONS: <location1>, <location2>, <location3>
NPC 1: <Name> - <Goal>
NPC 2: <Name> - <Goal>
NPC 3: <Name> - <Goal>

World concept:
{prompt}
"""

    response = groq_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": system_prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content
    print("RAW WORLD OUTPUT:\n", content)

    return parse_world(content)


def parse_world(text):
    world = {
        "name": "Unknown World",
        "description": "No description generated.",
        "locations": [],
        "npcs": []
    }

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line.lower().startswith("world name"):
            world["name"] = line.split(":")[-1].strip()

        elif line.lower().startswith("description"):
            world["description"] = line.split(":")[-1].strip()

        elif line.lower().startswith("locations"):
            locs = line.split(":")[-1]
            world["locations"] = [l.strip() for l in locs.split(",")]

        elif line.lower().startswith("npc"):
            try:
                parts = line.split(":")[1].split("-")
                world["npcs"].append({
                    "name": parts[0].strip(),
                    "goal": parts[1].strip()
                })
            except:
                continue

    return world