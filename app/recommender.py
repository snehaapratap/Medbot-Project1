recommendations = {
    "POSITIVE": ["Keep journaling your positive thoughts!", "Take a mindful walk."],
    "NEGATIVE": ["Try a breathing exercise.", "Consider writing down your feelings."],
    "NEUTRAL": ["Practice gratitude journaling.", "Do 10 minutes of stretching."]
}

def get_recommendation(sentiment_label):
    import random
    return random.choice(recommendations.get(sentiment_label, recommendations["NEUTRAL"]))
