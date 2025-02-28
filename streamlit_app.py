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
    response = openai.ChatCompletion.create(
    model="gpt-4-turbo",  # Use the latest available model
    messages=[
        {"role": "system", "content": "You are an academic AI moderator, providing fact-checking, logic analysis, and argument structuring."},
        {"role": "user", "content": prompt}
    )
    return response["choices"][0]["message"]["content"]

# Fetch messages in real-time
def get_messages():
    docs = chat_ref.order_by("timestamp").stream()
    return [{"user": doc.to_dict()["user"], "message": doc.to_dict()["message"]} for doc in docs]

st.title("💬 Discurs.eu")
st.write("Engage in live, AI-assisted discussions with real-time message updates.")

# Display messages
messages = get_messages()
for msg in messages:
    st.write(f"{msg['user']}: {msg['message']}")

# Input for new message
user_input = st.text_input("Your message:")
if st.button("Send") and user_input:
    chat_ref.add({
        "user": "You",
        "message": user_input,
        "timestamp": datetime.utcnow()
    })
    st.rerun()  # Refresh chat instantly

# AI Interventions
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🧐 Fact-Check"):
        fact_prompt = f"Fact-check this statement and provide reliable sources if possible: {user_input}"
        fact_response = ask_openai(fact_prompt)
        st.write(f"🧐 Fact-Check Result: {fact_response}")

with col2:
    if st.button("🧠 Logic Check"):
        logic_prompt = f"Analyze the logical coherence of this statement and identify any fallacies: {user_input}"
        logic_response = ask_openai(logic_prompt)
        st.write(f"🧠 Logic Check Result: {logic_response}")

with col3:
    if st.button("📖 Argument Structure"):
        argument_prompt = f"Evaluate the argument structure of this statement and suggest improvements: {user_input}"
        argument_response = ask_openai(argument_prompt)
        st.write(f"📖 Argument Analysis: {argument_response}")

# AI Flagging System (Passive Mode)
if os.getenv("ENABLE_FLAGGING") == "true":  # Example flag control
    st.warning("⚠️ AI has flagged a statement as potentially problematic.")
    if st.button("Explain Flag"):
        flag_prompt = f"Explain why this statement might be misleading or logically flawed: {user_input}"
        flag_response = ask_openai(flag_prompt)
        st.write(f"AI Explanation: {flag_response}")
