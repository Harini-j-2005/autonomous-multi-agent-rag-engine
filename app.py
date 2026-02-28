from world import WorldState
from agents import NPCAgent
from game_master import GameMaster
import time

def main():
    world = WorldState()
    game_master = GameMaster()

    # Multi-agent setup
    npc1 = NPCAgent("Ravi", "Steal the temple treasure")
    npc2 = NPCAgent("Arjun", "Protect the temple treasure")

    agents = [npc1, npc2]

    for turn in range(5):
        print(f"\n========== Autonomous Turn {turn} ==========")

        agent_explanations = []

        for agent in agents:
            explanation = agent.reason(world)
            print(f"\n🧠 {agent.name} reasoning:\n{explanation}")
            agent_explanations.append({agent.name: explanation})

        outcome = game_master.resolve_conflict(world, agent_explanations)

        print(f"\n🎭 Game Master Outcome:\n{outcome}")

        world.log_event(outcome)
        world.increase_tension()

        world_event = game_master.inject_world_event(world)
        if world_event:
            print(f"\n🌪 World Event: {world_event}")

        time.sleep(2)

    print("\n========== Final World State ==========")
    print(world.locations)
    print("Final Tension Level:", world.tension)

if __name__ == "__main__":
    main()