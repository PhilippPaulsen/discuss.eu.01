import streamlit as st
from utils import apply_custom_styles  # Import global styles

apply_custom_styles()  # Apply font styles

st.title("🟢 Agora - Open Discussions")
st.write("Welcome to the **Agora**! Engage in open-ended discussions with minimal AI moderation.")

# Input for discussion
user_input = st.text_input("Share your thoughts:")
if st.button("Post"):
    st.write(f"🗣️ You: {user_input}")

st.info("🔹 In Agora, AI assists **only when explicitly requested**.")
