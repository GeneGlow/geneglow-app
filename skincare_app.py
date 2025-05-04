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
import streamlit as st

# PAGE SETUP
st.set_page_config(page_title="GeneGlow Skincare - Login", layout="centered")

# CUSTOM CSS
st.markdown("""
    <style>
        .stApp {background-color: #FFFDF6; font-family: 'Segoe UI', sans-serif;}
        .stTextInput, .stButton > button {border-radius: 10px; padding: 0.5em;}
        .stButton > button {background-color: #FFD700; color: #2C2C2C;}
    </style>
""", unsafe_allow_html=True)

# Login Form
st.markdown('<div class="title">GeneGlow Login</div>', unsafe_allow_html=True)

email = st.text_input("Email Address")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # Here you would check credentials (this is just an example, in a real app, you would use a database)
    if email == "test@example.com" and password == "password":
        st.session_state.page = "quiz"
        st.experimental_rerun()
    else:
        st.error("Invalid credentials. Please try again.")

# Option to register if the user doesn't have an account
if st.button("Don't have an account? Sign up"):
    st.session_state.page = "signup"
    st.experimental_rerun()
import streamlit as st

# PAGE SETUP
st.set_page_config(page_title="GeneGlow Skincare Quiz", layout="centered")

# CUSTOM CSS
st.markdown("""
    <style>
        .stApp {background-color: #FFFDF6; font-family: 'Segoe UI', sans-serif;}
        .stButton > button {background-color: #FFD700; color: #2C2C2C; border-radius: 10px; padding: 0.5em;}
        .stButton > button:hover {background-color: #00CFC1; color: white;}
    </style>
""", unsafe_allow_html=True)

# Quiz Content
st.title("🌸 GeneGlow Skin Quiz")
st.subheader("Discover your skin type and learn how to reverse aging naturally.")

# Ask more in-depth questions
age = st.slider("How old are you?", 12, 80, 20)
skin_type = st.selectbox("What best describes your skin?", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])
concern = st.text_area("What is your biggest skin concern? (e.g., fine lines, acne, wrinkles, etc.)")

# Tips based on answers
if st.button("Get My Skin Report"):
    st.success("Thank you for completing the quiz! Here's how to reverse aging and improve your skin:")
    
    if skin_type == "Oily":
        st.markdown("- Use a gentle foaming cleanser with salicylic acid to clear pores.")
        st.markdown("- Incorporate Vitamin C for brighter skin and anti-aging.")
    elif skin_type == "Dry":
        st.markdown("- Hydrate with a rich moisturizer, and use hyaluronic acid.")
        st.markdown("- Avoid hot showers, they can dry out your skin further.")
    # More tailored advice for each skin type...

    st.markdown("### Anti-Aging Tips:")
    st.markdown("- Apply sunscreen daily (even indoors!). UV rays age skin.")
    st.markdown("- Incorporate retinol into your night routine for smoother skin.")
    st.markdown("- Drink plenty of water and eat foods rich in antioxidants.")

import streamlit as st

# PAGE SETUP
st.set_page_config(page_title="GeneGlow Skincare Quiz", layout="centered")

# CUSTOM CSS
st.markdown("""
    <style>
        .stApp {background-color: #FFFDF6; font-family: 'Segoe UI', sans-serif;}
        .stButton > button {background-color: #FFD700; color: #2C2C2C; border-radius: 10px; padding: 0.5em;}
        .stButton > button:hover {background-color: #00CFC1; color: white;}
    </style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🌸 GeneGlow Skin Quiz")
st.subheader("Discover your skin type and learn how to reverse aging naturally.")

# User inputs (with country selection)
age = st.slider("How old are you?", 12, 80, 20)
skin_type = st.selectbox("What best describes your skin?", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])
concern = st.text_area("What is your biggest skin concern? (e.g., fine lines, acne, wrinkles, etc.)")
country = st.selectbox("Which country are you from?", ["USA", "UK", "India", "Pakistan", "Australia", "Canada", "Other"])

# Tips based on answers
if st.button("Get My Skin Report"):
    st.success("Thank you for completing the quiz! Here's how to reverse aging and improve your skin:")

    # Home remedies and product recommendations based on skin type and country
    if skin_type == "Oily":
        st.markdown("- Use a gentle foaming cleanser with salicylic acid to clear pores.")
        st.markdown("- Incorporate Vitamin C for brighter skin and anti-aging.")
        st.markdown("**Home Remedy**: Use aloe vera gel or green tea as a face mask for oil control.")
    elif skin_type == "Dry":
        st.markdown("- Hydrate with a rich moisturizer, and use hyaluronic acid.")
        st.markdown("- Avoid hot showers, they can dry out your skin further.")
        st.markdown("**Home Remedy**: Honey and olive oil mask to hydrate dry skin.")
    elif skin_type == "Combination":
        st.markdown("- Use different products for T-zone vs cheeks.")
        st.markdown("**Home Remedy**: A cucumber mask can soothe both dry and oily skin.")
    elif skin_type == "Sensitive":
        st.markdown("- Use fragrance-free and gentle products.")
        st.markdown("**Home Remedy**: Chamomile tea bags for calming irritated skin.")
    
    # Reverse aging tips
    st.markdown("### Anti-Aging Tips:")
    st.markdown("- Apply sunscreen daily (even indoors!). UV rays age skin.")
    st.markdown("- Incorporate retinol into your night routine for smoother skin.")
    st.markdown("- Drink plenty of water and eat foods rich in antioxidants.")
    
    # Product Recommendations by Country
    if country == "USA":
        st.markdown("### Recommended Products in the USA:")
        st.markdown("- Neutrogena Oil-Free Acne Wash")
        st.markdown("- Olay Regenerist Micro-Sculpting Cream (Anti-aging)")
    elif country == "UK":
        st.markdown("### Recommended Products in the UK:")
        st.markdown("- The Ordinary Niacinamide 10% + Zinc 1%")
        st.markdown("- Eucerin Q10 Anti-Wrinkle Face Cream")
    elif country == "India":
        st.markdown("### Recommended Products in India:")
        st.markdown("- Himalaya Herbals Purifying Neem Face Wash")
        st.markdown("- Biotique Bio Wheat Germ Anti-Aging Cream")
    elif country == "Pakistan":
        st.markdown("### Recommended Products in Pakistan:")
        st.markdown("- Nivea Men Dark Spot Reduction Face Wash")
        st.markdown("- POND’S Age Miracle Wrinkle Corrector Night Cream")
    elif country == "Australia":
        st.markdown("### Recommended Products in Australia:")
        st.markdown("- Sukin Foaming Facial Cleanser")
        st.markdown("- Aesop Parsley Seed Anti-Oxidant Serum")
    elif country == "Canada":
        st.markdown("### Recommended Products in Canada:")
        st.markdown("- Neutrogena Hydro Boost Water Gel")
        st.markdown("- Kiehl’s Midnight Recovery Concentrate")
    else:
        st.markdown("### Recommended Products for Your Country:")
        st.markdown("- Research local skincare brands or online options that work for your skin concerns.")

