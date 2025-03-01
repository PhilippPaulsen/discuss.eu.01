import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
            @font-face {
                font-family: 'Suisse';
                src: url('/static/assets/SuisseIntl-Regular.woff2') format('woff2');
                font-weight: normal;
                font-style: normal;
            }

            @font-face {
                font-family: 'Suisse';
                src: url('/static/assets/SuisseIntl-Bold.woff2') format('woff2');
                font-weight: bold;
                font-style: normal;
            }

            html, body, [class*="st-"], h1, h2, h3, h4, h5, h6 {
                font-family: 'Suisse', sans-serif !important;
            }

            h1 {
                font-weight: 700;
            }
            h2, h3, h4, h5, h6 {
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)
