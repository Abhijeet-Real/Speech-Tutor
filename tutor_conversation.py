# Final version of app.py with enhanced layout, prompt fix, and gradient UI
from whisper_engine import transcribe
from grammar_corrector import get_corrected_grammar, get_speech_feedback, compare_answers

# --- Full agentic flow ---
def tutor_conversation(audio, question, ideal_answer, difficulty, model):
    if not audio:
        return "❌ No audio received", "", "", ""

    transcript, flagged_words = transcribe(audio)
    if not transcript:
        return "❌ No speech detected", "", "", ""

    grammar_output = get_corrected_grammar(transcript, question=question, model=model)
    feedback_output = get_speech_feedback(flagged_words, transcript=transcript, question=question, model=model)
    comparison = compare_answers(transcript, ideal_answer, model=model)

    return transcript, grammar_output, feedback_output, comparison