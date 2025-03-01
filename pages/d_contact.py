import streamlit as st

st.title("📞 Contact & Support")

st.write("For support, feedback, or inquiries, please reach out to us.")

st.text_area("📝 Your Message")
if st.button("Submit"):
    st.success("✅ Your message has been sent!")

st.info("🔹 Alternatively, you can reach us at contact@discurs.eu")
