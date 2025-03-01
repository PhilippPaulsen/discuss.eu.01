import streamlit as st

st.set_page_config(page_title="Discurs.eu", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Agora", "Forum", "Lab", "Invite Users", "Sign In", "Contact"])

if page == "Agora":
    import pages.agora
elif page == "Forum":
    import pages.forum
elif page == "Lab":
    import pages.lab
elif page == "Invite Users":
    import pages.invite
elif page == "Sign In":
    import pages.sign_in
elif page == "Contact":
    import pages.contact
