import streamlit as st

# ----- PAGE SETUP -----
st.set_page_config(page_title="GeneGlow Skincare", layout="centered")

# ----- CUSTOM CSS -----
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp {background-color: #FFFDF6; font-family: 'Segoe UI', sans-serif;}
        .title {text-align: center; font-size: 48px; font-weight: bold; color: #2C2C2C;}
        .subtitle {text-align: center; font-size: 20px; color: #00CFC1; margin-bottom: 30px;}
        .stButton > button {
            background-color: #FFD700; color: #2C2C2C;
            border-radius: 30px; padding: 0.5em 2em; font-weight: 600; transition: 0.3s ease;
        }
        .stButton > button:hover {background-color: #00CFC1; color: white;}
        .stTextInput, .stSelectbox, .stTextArea {
            background-color: #F8F9FA; border-radius: 10px; padding: 0.5em;
        }
    </style>
""", unsafe_allow_html=True)

# ----- HEADER -----
st.markdown('<div class="title">GeneGlow</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Glow Smarter. Naturally.</div>', unsafe_allow_html=True)

# ----- SKIN QUIZ -----
st.subheader("✨ Let's discover your perfect skincare routine!")

age = st.slider("How old are you?", 12, 60, 20)
oiliness = st.selectbox("Describe your skin's oil level:", ["Very Oily", "Oily", "Normal", "Dry", "Very Dry"])
sensitivity = st.selectbox("How sensitive is your skin?", ["Very Sensitive", "Somewhat Sensitive", "Not Sensitive"])
acne = st.selectbox("Do you get acne or breakouts?", ["Frequently", "Occasionally", "Rarely", "Never"])
climate = st.selectbox("What's your usual climate?", ["Hot & Humid", "Cold & Dry", "Mild", "Polluted Urban Area"])

# ----- LOGIC -----
def get_skin_type(oiliness, sensitivity):
    if oiliness in ["Very Oily", "Oily"] and sensitivity == "Not Sensitive":
        return "Oily"
    elif oiliness == "Normal":
        return "Normal"
    elif oiliness in ["Dry", "Very Dry"] and sensitivity != "Not Sensitive":
        return "Dry & Sensitive"
    else:
        return "Combination"

def get_recommendations(skin_type, acne):
    recs = []
    if skin_type == "Oily":
        recs.append("Use a foaming cleanser with salicylic acid.")
        recs.append("Try niacinamide serum to balance oil.")
    elif skin_type == "Dry & Sensitive":
        recs.append("Use a cream-based cleanser with ceramides.")
        recs.append("Hydrate with hyaluronic acid and a rich moisturizer.")
    elif skin_type == "Normal":
        recs.append("Maintain with gentle cleanser and light moisturizer.")
    elif skin_type == "Combination":
        recs.append("Use different products for T-zone vs cheeks.")

    if acne == "Frequently":
        recs.append("Add benzoyl peroxide or adapalene once daily.")
    elif acne == "Occasionally":
        recs.append("Spot-treat with tea tree oil or sulfur masks.")

    return recs

# ----- SHOW RESULTS -----
if st.button("🧬 Get My Skin Report"):
    skin_type = get_skin_type(oiliness, sensitivity)
    st.success(f"Your Skin Type: **{skin_type}**")

    st.markdown("### 🌿 Your Biotech-Backed Recommendations:")
    for rec in get_recommendations(skin_type, acne):
        st.markdown(f"- {rec}")
