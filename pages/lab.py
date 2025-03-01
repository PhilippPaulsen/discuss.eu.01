import streamlit as st
from utils import apply_custom_styles  # Import the styling function

st.set_page_config(page_title="Discurs.eu", page_icon="💬", layout="wide")

# Custom Title
st.markdown("""
    <h1 style='text-align: left; font-family: "Suisse", sans-serif; font-weight: bold;'>
        🔬 Lab - Research & Problem Solving
    </h1>
""", unsafe_allow_html=True)

st.write("Welcome to the **Lab**! Discussions here follow a structured research methodology.")

# Problem-solving workflow
st.subheader("Problem Representation")
st.text_area("📝 Define the Research Question")

st.subheader("Hypothesis Formulation")
st.text_area("🔍 State a Hypothesis")

st.subheader("Methodology")
st.text_area("🛠️ Describe the Research Method")

st.warning("⚠️ In Lab, **AI automatically assists in structuring discussions and ensuring clarity.**")
