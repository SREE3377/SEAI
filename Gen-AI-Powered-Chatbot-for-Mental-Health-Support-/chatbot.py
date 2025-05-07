import os
from groq import Groq
import streamlit as st

# Initialize the Groq client with your API key
client = Groq(api_key=os.environ.get("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"))

# Function to generate a response using LLaMA on Groq
def get_response(user_input):
    try:
        # Create a chat completion request using the Groq-specific model
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama-3.1-70b-versatile",  # Ensure this is correct
        )

        # Print full response for debugging
        st.write(f"Full response: {chat_completion}")

        # Return the generated response from the API
        return chat_completion['choices'][0]['message']['content'].strip()

    except Exception as e:
        st.error(f"Error occurred: {e}")
        return "Sorry, I couldn't process your request."

