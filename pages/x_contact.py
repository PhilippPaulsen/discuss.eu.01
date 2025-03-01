import streamlit as st
from utils import apply_custom_styles  # Import the styling function

st.set_page_config(page_title="Discurs.eu", page_icon="💬", layout="wide")

# Custom Title
st.markdown("""
    <h1 style='text-align: left; font-family: "Suisse", sans-serif; font-weight: bold;'>
        📞 Contact & Support
    </h1>
""", unsafe_allow_html=True)

st.write("For support, feedback, or inquiries, please reach out to us.")

st.text_area("📝 Your Message")
if st.button("Submit"):
    st.success("✅ Your message has been sent!")

st.info("🔹 Alternatively, you can reach us at contact@discurs.eu")
