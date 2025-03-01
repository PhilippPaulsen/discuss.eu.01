import streamlit as st

st.set_page_config(page_title="Discurs.eu", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Agora", "Forum", "Lab", "Contact", "Sign In"])

# Multi-page Navigation
if page == "Agora":
    import pages.a_agora
elif page == "Forum":
    import pages.b_forum
elif page == "Lab":
    import pages.c_lab
elif page == "Contact":
    import pages.d_contact
elif page == "Sign In":
    import pages.e_sign_in
