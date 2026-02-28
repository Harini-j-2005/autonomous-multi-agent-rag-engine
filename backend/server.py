from fastapi import FastAPI
from pydantic import BaseModel
from world_builder import build_world_from_prompt
from world import WorldState
from agents import NPCAgent
from game_master import GameMaster
from memory import MemorySystem
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory = MemorySystem()
game_master = GameMaster()

world = None
agents = []

class WorldPrompt(BaseModel):
    prompt: str

class TurnInput(BaseModel):
    action: str


@app.post("/create-world")
def create_world(data: WorldPrompt):
    global world, agents

    world_data = build_world_from_prompt(data.prompt)

    world = WorldState(
        world_data["name"],
        world_data["description"],
        world_data["locations"]
    )

    agents = []
    for npc in world_data["npcs"]:
        agents.append(NPCAgent(npc["name"], npc["goal"], memory))

    return world_data


@app.post("/turn")
def play_turn(data: TurnInput):
    agent_outputs = []

    for agent in agents:
        reasoning = agent.reason(world, data.action)
        agent_outputs.append(f"{agent.name}: {reasoning}")

    outcome = game_master.resolve(world, data.action, agent_outputs)
    memory.store(outcome)

    return {
        "tension": world.tension,
        "outcome": outcome,
        "agents": agent_outputs
    }