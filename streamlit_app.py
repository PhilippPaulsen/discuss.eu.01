import streamlit as st

# Set the page title & remove "Streamlit app" from navigation
st.set_page_config(page_title="Discurs.eu", page_icon="💬", layout="wide")

# Custom App Title (instead of "Streamlit app")
st.markdown("<h1 style='text-align: left;'>💬 Discurs.eu</h1>", unsafe_allow_html=True)
st.write("An AI-assisted discussion platform for rational and structured discourse.")

st.info("🔹 Use the sidebar to navigate between Agora, Forum, Lab, and other sections.")
