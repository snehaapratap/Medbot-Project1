from transformers import pipeline

chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def get_bot_response(user_input, history=[]):
    from transformers import Conversation
    conversation = Conversation(user_input)
    for utt in history:
        conversation.add_user_input(utt)
    result = chatbot(conversation)
    return str(result), history + [user_input]
