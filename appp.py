import streamlit as st
import requests

st.title("🧠 AI Mental Health Assistant")
msg = st.text_input("You: ", "")

if msg:
    response = requests.post("http://localhost:8000/chat/", json={"message": msg}).json()
    st.write(f"Assistant: {response['bot_reply']}")
    st.write(f"Sentiment: {response['sentiment']['label']}")
    st.write(f"Recommendation: {response['recommendation']}")
    st.write("📘 Resources:")
    for name, link in response["resources"].items():
        st.markdown(f"- [{name}]({link})")
