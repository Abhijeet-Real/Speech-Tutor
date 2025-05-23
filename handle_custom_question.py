import gen_QnA  

def handle_custom_question(choice_mode, current_question, topic, difficulty, model):
    """
    Handles custom question input:
    - If in custom topic mode and question is already populated, use that question
    - Otherwise, generate a new question and ideal answer
    """
    if choice_mode == "Enter custom topic" and current_question.strip():
        # Return the existing question and a placeholder for ideal answer
        return current_question, "This is a custom question. No ideal answer reference is available."
    else:
        # Generate a new question and ideal answer
        return gen_QnA.generate_question_and_answer(topic, difficulty, model)