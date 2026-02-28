from config import groq_client, MODEL_NAME

class NPCAgent:
    def __init__(self, name, goal, memory):
        self.name = name
        self.goal = goal
        self.memory = memory

    def reason(self, world, player_action):
        memories = self.memory.retrieve(self.goal)

        prompt = f"""
        You are {self.name}.
        Your goal: {self.goal}
        World tension: {world.tension}
        Player action: {player_action}
        Relevant memories: {memories}

        Explain your reasoning and what you attempt.
        """

        response = groq_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content