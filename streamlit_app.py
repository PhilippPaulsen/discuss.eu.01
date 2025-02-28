import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import os

# Load Firebase credentials from Streamlit secrets
firebase_credentials = st.secrets["FIREBASE_CREDENTIALS"]

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials)
    firebase_admin.initialize_app(cred)

db = firestore.client()
chat_ref = db.collection("messages")

# Fetch messages in real-time
def get_messages():
    docs = chat_ref.order_by("timestamp").stream()
    return [{"user": doc.to_dict()["user"], "message": doc.to_dict()["message"]} for doc in docs]

st.title("💬 Discurs.eu - Agora Mode (Real-Time Chat)")
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
    st.experimental_rerun()  # Refresh chat instantly

# AI Interventions
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🧐 Fact-Check"):
        st.write("AI Fact-Check: Placeholder response")
with col2:
    if st.button("🧠 Logic Check"):
        st.write("AI Logic Check: Placeholder response")
with col3:
    if st.button("📖 Argument Structure"):
        st.write("AI Argument Structure Analysis: Placeholder response")

# AI Flagging System (Passive Mode)
if os.getenv("ENABLE_FLAGGING") == "true":  # Example flag control
    st.warning("⚠️ AI has flagged a statement as potentially problematic.")
    if st.button("Explain Flag"):
        st.write("AI Explanation: Placeholder reasoning for flagged message.")
