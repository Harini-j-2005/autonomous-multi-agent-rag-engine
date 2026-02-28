import streamlit as st
from world import WorldState
from agents import NPCAgent
from game_master import GameMaster
from memory import MemorySystem

st.set_page_config(page_title="Multi-Agent Agentic RAG System", layout="wide")
st.title("🧠 Multi-Agent Autonomous RAG Game Master")

# Initialize
if "world" not in st.session_state:
    st.session_state.world = WorldState()
    st.session_state.memory = MemorySystem()
    st.session_state.game_master = GameMaster()

    st.session_state.agents = [
        NPCAgent("Ravi", "Steal the temple treasure", st.session_state.memory),
        NPCAgent("Arjun", "Protect the temple treasure", st.session_state.memory)
    ]

    st.session_state.logs = []

world = st.session_state.world
memory = st.session_state.memory
game_master = st.session_state.game_master
agents = st.session_state.agents

# Player Input
st.sidebar.header("🎮 Player Turn")
player_action = st.sidebar.text_input("What do you do?")

if st.sidebar.button("Submit Turn") and player_action:
    turn_log = "\n========== New Turn ==========\n"
    turn_log += f"\n👤 Player Action:\n{player_action}\n"

    agent_explanations = []

    for agent in agents:
        explanation = agent.reason(world, player_action)
        turn_log += f"\n🧠 {agent.name} Reasoning:\n{explanation}\n"
        agent_explanations.append({agent.name: explanation})

    outcome = game_master.resolve_turn(world, player_action, agent_explanations)
    turn_log += f"\n🎭 Game Master Outcome:\n{outcome}\n"

    # Store in memory (RAG Update)
    memory.store(f"Player: {player_action}")
    memory.store(outcome)

    world.log_event(outcome)
    world.increase_tension()

    world_event = game_master.inject_world_event(world)
    if world_event:
        memory.store(world_event)
        turn_log += f"\n🌪 World Event:\n{world_event}\n"

    st.session_state.logs.append(turn_log)

# Display world
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 World State")
    st.write(world.locations)
    st.write("Tension:", world.tension)
    st.write("Player Reputation:", world.player["reputation"])
    st.progress(min(world.tension / 10, 1.0))

with col2:
    st.subheader("📜 Simulation Log")
    for log in reversed(st.session_state.logs):
        st.text(log)