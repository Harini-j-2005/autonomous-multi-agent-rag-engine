from config import groq_client, MODEL_NAME

class NPCAgent:
    def __init__(self, name, goal, memory):
        self.name = name
        self.goal = goal
        self.memory = memory

    def reason(self, world, player_action):
        retrieved_memories = self.memory.retrieve(
            f"{self.goal} {player_action}"
        )

        prompt = f"""
        You are {self.name}.
        Your goal: {self.goal}

        Player Action:
        {player_action}

        Retrieved Relevant Memories:
        {retrieved_memories}

        Current World:
        {world.locations}
        Tension: {world.tension}
        Player Reputation: {world.player['reputation']}

        Think step-by-step:
        1. What memories influence you?
        2. How does player action affect you?
        3. What do you attempt?
        4. Why?

        Be logical and consistent.
        """

        response = groq_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a goal-driven autonomous agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        return response.choices[0].message.content