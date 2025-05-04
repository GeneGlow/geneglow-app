import streamlit as st

# PAGE SETUP
st.set_page_config(page_title="GeneGlow Skincare", layout="centered")

# CUSTOM CSS (to make the page look clean)
st.markdown("""
    <style>
        .stApp {background-color: #FFFDF6; font-family: 'Segoe UI', sans-serif;}
        .title {text-align: center; font-size: 48px; font-weight: bold; color: #2C2C2C;}
        .subtitle {text-align: center; font-size: 20px; color: #00CFC1; margin-bottom: 30px;}
        .stButton > button {background-color: #FFD700; color: #2C2C2C; border-radius: 30px; padding: 0.5em 2em;}
        .stButton > button:hover {background-color: #00CFC1; color: white;}
    </style>
""", unsafe_allow_html=True)

# WELCOME PAGE
st.markdown('<div class="title">Welcome to GeneGlow Skincare</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Personalized Skincare Journey Starts Here!</div>', unsafe_allow_html=True)

# Introduction text
st.markdown("""
    GeneGlow is designed to provide tailored skincare solutions for your skin's unique needs. 
    We combine the power of **biotechnology** and **natural remedies** to reverse aging and keep you glowing at any age. 
    Our quiz will guide you step-by-step toward understanding your skin type and how to achieve healthier, younger skin at home.

    Ready to begin? Start by logging in and let us help you glow smarter.
""")

# Button to proceed to login
if st.button("Get Started"):
    # Redirect to login page (will be part of the next steps)
    st.session_state.page = "login"  # We'll handle routing later
    st.experimental_rerun()
