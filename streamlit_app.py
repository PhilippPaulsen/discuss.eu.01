import streamlit as st
import openai
from datetime import datetime
import random

# OpenAI API Key (Replace with your key or load it securely)
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Initialize session state for chat history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = "Agora"

# Sidebar for settings
st.sidebar.title("Settings")
st.sidebar.write("Select discussion mode:")
mode = st.sidebar.selectbox("Mode", ["Agora", "Forum", "Lab"])
st.session_state.selected_mode = mode

# Chat UI
st.title("💬 Discurs.eu")
st.write(f"🛠️ Mode: **{mode}** (Click dropdown in sidebar to switch)")

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(f"{msg['name']}: {msg['content']}")
    else:
        st.chat_message("assistant").write(msg['content'])

# User input
user_input = st.text_input("Your message:", key="user_input")
if st.button("Send") and user_input:
    user_name = "You"
    st.session_state.messages.append({"role": "user", "name": user_name, "content": user_input})
    st.chat_message("user").write(f"{user_name}: {user_input}")
    
    # AI intervention buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🧐 Fact-Check"):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": f"Fact-check this statement: {user_input}"}]
            )
            fact_check_result = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": fact_check_result})
            st.chat_message("assistant").write(fact_check_result)
    with col2:
        if st.button("🧠 Logic Check"):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": f"Analyze the logical coherence of this statement: {user_input}"}]
            )
            logic_result = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": logic_result})
            st.chat_message("assistant").write(logic_result)
    with col3:
        if st.button("📖 Argument Structure"):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": f"Evaluate the argument structure of this statement: {user_input}"}]
            )
            argument_result = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": argument_result})
            st.chat_message("assistant").write(argument_result)

# AI Flagging System
if random.random() < 0.2:  # 20% chance to flag a message
    st.warning("⚠️ AI has flagged this statement as potentially problematic. Click below to request an explanation.")
    if st.button("Explain Flag"):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Explain why this statement might be misleading or logically flawed: {user_input}"}]
        )
        flag_explanation = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": flag_explanation})
        st.chat_message("assistant").write(flag_explanation)
