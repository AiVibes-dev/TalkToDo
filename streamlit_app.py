import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Set page to wide mode
st.set_page_config(layout="wide")

# Load environment variables
load_dotenv()

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize menu state
if "menu_expanded" not in st.session_state:
    st.session_state.menu_expanded = True

# Initialize OpenRouter API key and model
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "google/gemini-2.0-flash-thinking-exp:free")

if not OPENROUTER_API_KEY:
    st.error("Please set your OpenRouter API key in the .env file")
    st.stop()

# Create three columns for the layout with 15-50-35 split
left_col, middle_col, right_col = st.columns([1, 3, 2], gap="small")

# Left column - Model info and settings
with left_col:
    st.title("TalkToDo")
    
    # Menu toggle button
    if st.button("☰" if st.session_state.menu_expanded else "☰"):
        st.session_state.menu_expanded = not st.session_state.menu_expanded
    
    # Menu items with icons and labels
    menu_items = [
        ("📝", "Tasks", ["New Task", "View Tasks"]),
        ("📁", "Projects", ["New Project", "View Projects"]),
        ("📅", "Calendar", ["Add Event", "View Calendar"]),
        ("⚙️", "Settings", ["Profile", "Preferences"]),
        ("📊", "Analytics", ["Reports", "Stats"])
    ]
    
    # Display menu items
    for icon, label, buttons in menu_items:
        if st.session_state.menu_expanded:
            st.markdown(f"### {icon} {label}")
            for button in buttons:
                st.button(button, key=f"{label}_{button}")
        else:
            st.markdown(f"### {icon}")
            if st.button(icon, key=f"icon_{label}"):
                st.session_state.menu_expanded = True
                st.rerun()

# Middle column - GTD section
with middle_col:
    st.title("GTD")
    st.write("Getting Things Done section coming soon...")
    # Placeholder for future GTD implementation
    st.markdown("""
    ### Inbox
    - [ ] Task 1
    - [ ] Task 2
    
    ### Projects
    - Project A
    - Project B
    
    ### Next Actions
    - Action 1
    - Action 2
    """)

# Right column - Chat interface
with right_col:
    st.title("Chat")
    
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
                    "HTTP-Referer": "https://aivibes.streamlit.app/",
                    "X-Title": "TalkToDo Chatbot"
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
                response.raise_for_status()
                
                # Extract the assistant's response
                assistant_response = response.json()["choices"][0]["message"]["content"]
                
                # Display and store the response
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

