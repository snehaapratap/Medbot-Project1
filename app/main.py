from fastapi import FastAPI, Request
from app.chatbot import get_bot_response
from app.sentiment import analyze_sentiment
from app.recommender import get_recommendation
from app.resources import get_resources

app = FastAPI()
chat_history = []

@app.post("/chat/")
async def chat(req: Request):
    body = await req.json()
    user_input = body["message"]

    bot_reply, updated_history = get_bot_response(user_input, chat_history)
    sentiment = analyze_sentiment(user_input)
    recommendation = get_recommendation(sentiment["label"])

    chat_history.extend([user_input, bot_reply])

    return {
        "bot_reply": bot_reply,
        "sentiment": sentiment,
        "recommendation": recommendation,
        "resources": get_resources()
    }
