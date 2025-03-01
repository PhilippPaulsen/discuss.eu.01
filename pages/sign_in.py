import streamlit as st

st.title("🔑 Sign In to Discurs.eu")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    st.success(f"✅ Welcome, {username}!")

st.warning("⚠️ Authentication system will be integrated in future versions.")
