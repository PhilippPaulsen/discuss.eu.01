import streamlit as st
from utils import apply_custom_styles  # Import the styling function

st.set_page_config(page_title="Discurs.eu", page_icon="💬", layout="wide")

# Custom Title
st.markdown("""
    <h1 style='text-align: left; font-family: "Suisse", sans-serif; font-weight: bold;'>
        🔵 Forum - Structured Debates
    </h1>
""", unsafe_allow_html=True)

st.write("Welcome to the **Forum**! Engage in structured discussions with ranking and voting features.")

# Discussion topic
st.subheader("Select a Discussion Topic")
topic = st.selectbox("Choose a category:", ["Ethics", "Science", "Politics", "Technology", "Education"])

# Voting system
st.write("⬆️⬇️ Vote on Key Arguments")
st.button("👍 Agree")
st.button("👎 Disagree")

st.info("🔹 In Forum, AI can **categorize arguments and highlight missing perspectives upon request**.")
