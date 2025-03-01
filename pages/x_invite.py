import streamlit as st
from utils import apply_custom_styles  # Import the styling function

st.set_page_config(page_title="Discurs.eu", page_icon="💬", layout="wide")

# Custom Title
st.markdown("""
    <h1 style='text-align: left; font-family: "Suisse", sans-serif; font-weight: bold;'>
        📩 Invite Users
    </h1>
""", unsafe_allow_html=True)

st.write("Send an invitation to new users to join a discussion on Discurs.eu.")

email = st.text_input("Enter Email Address")
if st.button("Send Invite"):
    st.success(f"✅ Invitation sent to {email}")

st.info("🔹 Users will receive an invite link via email.")
