import streamlit as st
from utils import apply_custom_styles  # Import the styling function

st.set_page_config(page_title="Discurs.eu", page_icon="💬", layout="wide")

# Custom Title
st.markdown("""
    <h1 style='text-align: left; font-family: "Suisse", sans-serif; font-weight: bold;'>
        🔑 Sign In to Discurs.eu
    </h1>
""", unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    st.success(f"✅ Welcome, {username}!")

st.warning("⚠️ Authentication system will be integrated in future versions.")
