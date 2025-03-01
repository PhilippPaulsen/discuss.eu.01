import streamlit as st
from utils import apply_custom_styles  # Import global styles

apply_custom_styles()  # Apply font styles

# Custom Title
st.markdown("""
    <h1 style='text-align: left; font-family: "Suisse", sans-serif; font-weight: bold;'>
        🟢 Agora - Open Discussions
    </h1>
""", unsafe_allow_html=True)

st.write("Welcome to the **Agora**! Engage in open-ended discussions with minimal AI moderation.")

# Input for discussion
user_input = st.text_input("Share your thoughts:")
if st.button("Post"):
    st.write(f"🗣️ You: {user_input}")

st.info("🔹 In Agora, AI assists **only when explicitly requested**.")
