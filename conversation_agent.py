# conversation_agent.py

from llm_engine import call_ollama

def simulate_conversation(user_input, role="Interviewer", topic="Technology", model="mistral:latest"):
    prompt = f"""
You are a {role} having a casual conversation with a language learner.

Topic: {topic}

The learner just said:
"{user_input}"

Respond in character as a {role}, based on the topic and what they said.

Instructions:
- Your response should feel like a follow-up in a real conversation.
- Keep it short (1-3 sentences), natural, and engaging.
- If their response is vague, ask for more details.
- If it's interesting, respond supportively or challenge them politely.
"""
    
    return call_ollama(prompt, model=model)
