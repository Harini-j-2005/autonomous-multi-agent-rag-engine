from config import groq_client, MODEL_NAME

class GameMaster:
    def resolve(self, world, player_action, agent_outputs):
        prompt = f"""
        Player action: {player_action}
        Agent intentions:
        {agent_outputs}

        Decide what actually happens in the world.
        Provide final outcome.
        """

        response = groq_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        outcome = response.choices[0].message.content
        world.increase_tension()
        world.log_event(outcome)
        return outcome