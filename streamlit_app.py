import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os
import openai

# Convert Streamlit secrets to a dictionary
firebase_credentials = dict(st.secrets["FIREBASE_CREDENTIALS"])  # Ensure correct format

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials)  # Use dict directly
    firebase_admin.initialize_app(cred)

db = firestore.client()
chat_ref = db.collection("messages")

# OpenAI API Key
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def ask_openai(prompt):
    """Sends a query to OpenAI and returns the response."""
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are an academic AI participant, engaging in logical, fact-based discussions."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Fetch messages in real-time
def get_messages():
    docs = chat_ref.order_by("timestamp").stream()
    return [{"user": doc.to_dict()["user"], "message": doc.to_dict()["message"]} for doc in docs]

st.title("💬 Discurs.eu")
st.write("Engage in live, AI-assisted discussions with real-time message updates.")

# Fetch messages before looping
messages = get_messages()

# AI Conversation Partner - Responds to each user input
if messages and messages[-1]["user"] == "You":
    ai_response = ask_openai(messages[-1]["message"])
    chat_ref.add({
        "user": "AI", 
        "message": ai_response, 
        "timestamp": datetime.utcnow()
    })
    messages.append({"user": "AI", "message": ai_response})

# Display messages in speech bubbles with adaptive width and right-aligned user messages
for msg in messages:
    user_name = msg['user']
    message_content = msg['message']
    
    # Determine indentation based on message length (max indent 40px)
    indent_level = min(len(message_content) // 50, 8) * 5  # Increments of 5px, max 40px
    indent_style = f"margin-left: auto; margin-right: {indent_level}px; text-align: left;" if user_name == "You" else "margin-left: 0px; margin-right: auto; text-align: left;"
    
    # Define color scheme
    if user_name == "You":
        bubble_style = "background-color: lightgray; color: black;"
    elif user_name.lower() == "ai":
        bubble_style = "background-color: #4D4D4D; color: white;"
    else:
        bubble_style = "background-color: lightgray; color: black;"
    
    st.markdown(f"""
    <div style='padding: 10px; border-radius: 15px; margin: 5px 0; {bubble_style} {indent_style} max-width: 75%; word-wrap: break-word; display: block; width: fit-content;'>
        <b>{user_name}:</b> {message_content}
    </div>
    """, unsafe_allow_html=True)

# Input for new message
user_input = st.text_input("Your message:")

# Arrange buttons
col1, col2 = st.columns([3, 1])
with col1:
    fact_col, logic_col, arg_col = st.columns(3)
    with fact_col:
        if st.button("🧐", help="Fact-check the last statement"):
            fact_prompt = f"Fact-check this statement and provide reliable sources if possible: {user_input}"
            fact_response = ask_openai(fact_prompt)
            st.write(f"🧐 Fact-Check Result: {fact_response}")
    with logic_col:
        if st.button("🧠", help="Analyze logic and detect fallacies"):
            logic_prompt = f"Analyze the logical coherence of this statement and identify any fallacies: {user_input}"
            logic_response = ask_openai(logic_prompt)
            st.write(f"🧠 Logic Check Result: {logic_response}")
    with arg_col:
        if st.button("📖", help="Evaluate argument structure"):
            argument_prompt = f"Evaluate the argument structure of this statement and suggest improvements: {user_input}"
            argument_response = ask_openai(argument_prompt)
            st.write(f"📖 Argument Analysis: {argument_response}")

with col2:
    post_col, save_col, new_col = st.columns(3)
    with post_col:
        if st.button("📩"):
            chat_ref.add({
                "user": "You",
                "message": user_input,
                "timestamp": datetime.utcnow()
            })
            st.rerun()
    with save_col:
        if st.button("💾", help="Save and download conversation"):
            conversation_text = "\n".join([f"{msg['user']}: {msg['message']}" for msg in messages])
            st.download_button(label="⬇️", data=conversation_text, file_name="discurs_chat.txt", mime="text/plain")
    with new_col:
        if st.button("🆕", help="Start a new conversation"):
            for doc in chat_ref.stream():
                doc.reference.delete()
            st.rerun()

# AI Flagging System (Passive Mode)
if os.getenv("ENABLE_FLAGGING") == "true":  # Example flag control
    flagged_prompt = f"Analyze this statement for misleading, false, or illogical content. If issues exist, flag them explicitly: {user_input}."
    flagged_response = ask_openai(flagged_prompt)
    if any(keyword in flagged_response.lower() for keyword in ["misleading", "false", "incorrect", "illogical", "inaccurate", "not true"]):
        st.warning("⚠️ AI has flagged this statement as potentially problematic.")
        if st.button("❓", help="Explain why this statement was flagged"):
            st.write(f"AI Explanation: {flagged_response}")
