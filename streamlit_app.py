import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize OpenRouter API key and model
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "google/gemini-2.0-flash-thinking-exp:free")  # Default to GPT-4 if not specified

if not OPENROUTER_API_KEY:
    st.error("Please set your OpenRouter API key in the .env file")
    st.stop()

st.title("TalkToDo")

# Display current model being used
st.sidebar.write(f"Current Model: {OPENROUTER_MODEL}")

st.write("This is a simple chatbot that can answer questions about the Do platform.")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add assistant response
    with st.chat_message("assistant"):
        try:
            # Prepare the API request
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/yourusername/TalkToDo",  # Replace with your actual site URL
                "X-Title": "TalkToDo Chatbot"  # Replace with your site name
            }
            
            # Convert chat history to the format expected by the API
            messages = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages]
            
            data = {
                "model": OPENROUTER_MODEL,
                "messages": messages,
                "temperature": 0.7
            }
            
            # Make the API request
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Extract the assistant's response
            assistant_response = response.json()["choices"][0]["message"]["content"]
            
            # Display and store the response
            st.markdown(assistant_response)
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            st.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

