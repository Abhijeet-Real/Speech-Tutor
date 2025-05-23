from string import Template
from llm_engine import call_ollama

# --- Generate question + ideal answer ---
def generate_question_and_answer(topic, difficulty, model):
    # Add a random seed to prevent repetition
    import random
    random_seed = random.randint(1, 10000)
    
    prompt = Template("""
You are a professor and recognized expert in "$topic".

Create a concise, precise speaking prompt at a "$difficulty" level. Your task:

1. Generate a BRIEF, focused question about "$topic" that:
   - Is intellectually stimulating but CONCISE (max 1-2 sentences)
   - Requires critical thinking appropriate for the difficulty level
   - Avoids vague or overly broad phrasing
   - Is DIFFERENT from standard/common questions on this topic

2. Difficulty guidelines:
   - Easy: Clear, accessible language about familiar concepts
   - Medium: Focused questions on specific concepts requiring explanation
   - Hard: Precise questions on advanced concepts requiring structured argument

3. Question format requirements:
   - BREVITY is essential - questions should be direct and to the point
   - For medium/hard levels, focus on SPECIFIC aspects rather than broad topics
   - Include a clear focus that guides the speaker

Output format:
Question: <Your concise, focused question - NO MORE THAN 1-2 SENTENCES>
Ideal Answer: <A well-structured response showing appropriate depth for the difficulty level>

IMPORTANT: 
- Use random seed $random_seed to ensure question variety
- Questions MUST be brief and precise
- Avoid lengthy, multi-part questions
- Focus on quality over quantity in both question and answer
""").substitute(topic=topic, difficulty=difficulty, random_seed=random_seed)

    # First attempt
    response = call_ollama(prompt, model=model)
    try:
        question, ideal = response.split("Ideal Answer:")
        question_text = question.replace("Question:", "").strip()
        
        # Verify we don't have an empty or default question
        if question_text and not question_text.lower().startswith("what do you think about"):
            return question_text, ideal.strip()
    except:
        pass  # Continue to fallback if there's an exception
    
    # Fallback with a more specific question based on topic and difficulty
    fallback_prompts = {
        "Easy": f"How has {topic} influenced your personal experiences?",
        "Medium": f"What are the most significant developments in {topic} in recent years?",
        "Hard": f"Analyze the critical challenges facing {topic} and propose potential solutions."
    }
    
    fallback_question = fallback_prompts.get(difficulty, f"Discuss a specific aspect of {topic} that interests you most.")
    fallback_answer = f"This would require a thoughtful response about {topic} appropriate for {difficulty} difficulty level."
    
    # Try one more time with a simpler prompt
    retry_prompt = f"Generate a single, concise question about {topic} at {difficulty} difficulty level."
    retry_response = call_ollama(retry_prompt, model=model)
    
    if len(retry_response) > 10 and "?" in retry_response:
        # Use the retry response if it looks reasonable
        return retry_response.strip(), fallback_answer
    
    # Use our fallback if all else fails
    return fallback_question, fallback_answer