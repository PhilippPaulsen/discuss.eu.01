import streamlit as st

st.title("🟢 Agora - Open Discussions")
st.write("Welcome to the **Agora**! Engage in open-ended discussions with minimal AI moderation.")

# Input for discussion
user_input = st.text_input("Share your thoughts:")
if st.button("Post"):
    st.write(f"🗣️ You: {user_input}")

st.info("🔹 In Agora, AI assists **only when explicitly requested**.")
