import streamlit as st

st.set_page_config(page_title="Discurs.eu", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Agora", "Forum", "Lab", "Contact", "Sign In"])

# Multi-page Navigation
if page == "Agora":
    import pages.01_agora
elif page == "Forum":
    import pages.02_forum
elif page == "Lab":
    import pages.03_lab
elif page == "Contact":
    import pages.04_contact
elif page == "Sign In":
    import pages.05_sign_in
