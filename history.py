# Function to save user history
import HuggingFaceLogin as HFL
import json
import datetime
from pathlib import Path

def save_history(user_id, topic, difficulty, question, transcript, grammar, feedback, comparison, rating):
    # Create history directory if it doesn't exist
    history_dir = Path("user_history")
    history_dir.mkdir(exist_ok=True)
    
    # Create user file if it doesn't exist
    user_file = history_dir / f"{user_id}.json"
    
    # Load existing history or create new
    if user_file.exists():
        with open(user_file, "r") as f:
            history = json.load(f)
    else:
        history = {"sessions": []}
    
    # Add new session
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_session = {
        "timestamp": timestamp,
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "transcript": transcript,
        "grammar_feedback": grammar,
        "pronunciation_feedback": feedback,
        "comparison_feedback": comparison,
        "rating": rating
    }
    
    history["sessions"].append(new_session)
    
    # Save updated history
    with open(user_file, "w") as f:
        json.dump(history, f, indent=2)
    
    return history

# Function to load user history
def load_history(user_id):
    history_file = Path("user_history") / f"{user_id}.json"
    if history_file.exists():
        with open(history_file, "r") as f:
            return json.load(f)
    return {"sessions": []}