import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env
# Initialize Groq client
from groq import Groq

# Pass the API key directly to the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function to apply local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the external CSS file
local_css("styles.css")

# Streamlit app UI
st.title("Mental Health ChatBot 🤖")
st.markdown("This is a *Generative AI* chatbot for mental health assistance.")

# Chat history
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Input mode selector (only Text now)
st.markdown("You can type your questions below.")

# Function to get response from the bot
def get_response(user_input):
    # Call Groq API to get chat completion
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama3-8b-8192",  # Use the appropriate model here
    )
    return chat_completion.choices[0].message.content  # Return the response content

# Text input
user_input = st.text_input("You:")

if st.button("Submit"):
    if user_input:
        # Get response from the chatbot
        response = get_response(user_input)

        # Save conversation to session history
        st.session_state['history'].append(f"You: {user_input}")
        st.session_state['history'].append(f"Bot: {response}")

        # Display chat history with styled messages
        for i, message in enumerate(st.session_state['history']):
            if i % 2 == 0:
                st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-message">{message}</div>', unsafe_allow_html=True)

# Button to clear chat history
if st.button("Clear History", key="clear_history"):
    st.session_state['history'] = []
    st.success("Chat history cleared.")