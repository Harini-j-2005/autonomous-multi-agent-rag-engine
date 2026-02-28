from config import groq_client, MODEL_NAME

class GameMaster:

    def resolve_turn(self, world, player_action, agent_explanations):
        prompt = f"""
        You are the Autonomous Game Master.

        Player Action:
        {player_action}

        Agent Intentions:
        {agent_explanations}

        Current World:
        {world.locations}
        Tension: {world.tension}
        Player Reputation: {world.player['reputation']}

        Decide what actually happens this turn.

        Update:
        - Does treasure change?
        - Does tension increase?
        - Does reputation change?
        - Any consequences?

        Explain clearly.
        """

        response = groq_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You control the simulation world fairly and logically."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        return response.choices[0].message.content

    def inject_world_event(self, world):
        if world.tension >= 3:
            world.increase_security()
            return "Temple security increases due to rising tension."
        return None