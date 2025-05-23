# Function to generate interview questions
from llm_engine import call_ollama

def generate_interview_questions(topic, personality_traits, technical_skills, model):
    prompt = f"""Generate 5 interview questions related to {topic} that would be appropriate for someone with the following traits:
    
Personality traits: {personality_traits}
Technical skills: {technical_skills}

For each question, provide:
1. The question itself (concise and clear)
2. A brief hint/guideline on how to approach answering it
3. Key points that should be included in a good answer

Format each question as:
Q: [Question text]
Hint: [Brief guidance on approaching the answer]
Key points: [Bullet points of important elements to include]

Make the questions varied in difficulty and approach.
"""
    
    response = call_ollama(prompt, model=model)
    return response