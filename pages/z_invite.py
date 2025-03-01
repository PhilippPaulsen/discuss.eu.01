import streamlit as st

st.title("📩 Invite Users")
st.write("Send an invitation to new users to join a discussion on Discurs.eu.")

email = st.text_input("Enter Email Address")
if st.button("Send Invite"):
    st.success(f"✅ Invitation sent to {email}")

st.info("🔹 Users will receive an invite link via email.")
