import streamlit as st

st.title("🔵 Forum - Structured Debates")
st.write("Welcome to the **Forum**! Engage in structured discussions with ranking and voting features.")

# Discussion topic
st.subheader("Select a Discussion Topic")
topic = st.selectbox("Choose a category:", ["Ethics", "Science", "Politics", "Technology", "Education"])

# Voting system
st.write("⬆️⬇️ Vote on Key Arguments")
st.button("👍 Agree")
st.button("👎 Disagree")

st.info("🔹 In Forum, AI can **categorize arguments and highlight missing perspectives upon request**.")
