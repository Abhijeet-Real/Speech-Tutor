# Function to calculate star rating based on feedback
def calculate_rating(transcript, grammar, feedback, comparison):
    # Simple algorithm to calculate rating between 1.0 and 5.0
    if not transcript:
        return 0
    
    # Base score
    score = 3.0
    
    # Add points for length (up to 0.5 points)
    words = len(transcript.split())
    if words > 50:
        score += 0.5
    elif words > 30:
        score += 0.3
    elif words > 15:
        score += 0.1
    
    # Check for grammar issues (subtract up to 0.7 points)
    if "no grammar issues" in grammar.lower() or "excellent grammar" in grammar.lower():
        score += 0.7
    elif "minor grammar issues" in grammar.lower():
        score += 0.3
    elif "several grammar issues" in grammar.lower():
        score -= 0.3
    else:
        score -= 0.5
    
    # Check pronunciation feedback (up to 0.5 points)
    if "excellent pronunciation" in feedback.lower() or "no pronunciation issues" in feedback.lower():
        score += 0.5
    elif "minor pronunciation issues" in feedback.lower():
        score += 0.2
    elif "several pronunciation issues" in feedback.lower():
        score -= 0.2
    else:
        score -= 0.4
    
    # Check comparison with ideal answer (up to 1.0 points)
    if "excellent response" in comparison.lower() or "outstanding answer" in comparison.lower():
        score += 1.0
    elif "good response" in comparison.lower() or "solid answer" in comparison.lower():
        score += 0.5
    elif "adequate response" in comparison.lower():
        score += 0.2
    elif "poor response" in comparison.lower():
        score -= 0.5
    
    # Ensure score is between 1.0 and 5.0
    score = max(1.0, min(5.0, score))
    
    # Round to one decimal place
    return round(score, 1)