import streamlit as st

# Set the page title & remove "Streamlit app" from navigation
st.set_page_config(page_title="Discurs.eu", page_icon="💬", layout="wide")

# Custom App Title (instead of "Streamlit app")
st.markdown("<h1 style='text-align: center;'>💬 Discurs.eu</h1>", unsafe_allow_html=True)

st.write("""
**Welcome to Discurs.eu!**

Discurs.eu is an AI-assisted discussion platform designed to **enhance rational, structured, and goal-oriented discourse.** 
Our platform enables users to engage in open discussions (**Agora**), structured debates (**Forum**), and research-oriented problem-solving (**Lab**) with AI-driven **fact-checking, logic validation, and argument structuring**.

### **How It Works**
- **Agora:** Free-form discussions with minimal AI intervention.
- **Forum:** Structured debates with argument categorization and ranking.
- **Lab:** Research-driven conversations with peer review and AI guidance.

Discurs.eu is built on ethical AI principles, fostering **transparent, constructive, and inclusive** conversations for academia, research, and civic engagement. 

🔹 **Use the sidebar to navigate between Agora, Forum, Lab, and other sections.**
""")
