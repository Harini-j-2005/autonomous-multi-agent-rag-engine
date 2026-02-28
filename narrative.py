from config import groq_client

def generate_narrative(event, memories=None):
    memory_text = ""

    if memories:
        memory_text = "\nRelevant past events:\n" + "\n".join(memories)

    prompt = f"""
    You are narrating a dynamic AI-driven simulation.

    Event: {event}

    {memory_text}

    Generate immersive but concise storytelling.
    """

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a cinematic game narrator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content