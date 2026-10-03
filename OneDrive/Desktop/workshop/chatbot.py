import os
import streamlit as st
from openai import OpenAI

# Page settings
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.write("Ask me anything!")

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY is not configured.")
    st.stop()

client = OpenAI(api_key=api_key)

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.responses.create(
                model="gpt-5-mini",
                input=user_input
            )

            answer = response.output_text
            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })