import streamlit as st

# ------------------- Page Config -------------------
st.set_page_config(page_title="GeneGlow Skincare Quiz", layout="centered")

# Custom styles
def set_bg_color():
    st.markdown("""
        <style>
        body {
            background-color: #F5F3FA;
        }
        .stButton>button {
            background-color: #CFA2ED;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            height: 40px;
        }
        </style>
        """, unsafe_allow_html=True)

set_bg_color()

# ------------------- App Logo & Title -------------------
st.title("🌸 GeneGlow: Personalized Skincare")
st.subheader("Where Biotech meets Beauty 💧")

# ------------------- Quiz -------------------
age = st.slider("How old are you?", 12, 60, 20)
oiliness = st.selectbox("Describe your skin's oil level:", ["Very Oily", "Oily", "Normal", "Dry", "Very Dry"])
sensitivity = st.selectbox("How sensitive is your skin?", ["Very Sensitive", "Somewhat Sensitive", "Not Sensitive"])
acne = st.selectbox("Do you get acne or breakouts?", ["Frequently", "Occasionally", "Rarely", "Never"])
climate = st.selectbox("What's your usual climate?", ["Hot & Humid", "Cold & Dry", "Mild", "Polluted Urban Area"])

# ------------------- Logic Functions -------------------
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

# ------------------- Button Action -------------------
if st.button("✨ Get My Skin Report"):
    skin_type = get_skin_type(oiliness, sensitivity)
    st.success(f"Your Skin Type: **{skin_type}**")

    st.markdown("### Your Biotech-Backed Recommendations:")
    for rec in get_recommendations(skin_type, acne):
        st.markdown(f"- {rec}")
import streamlit as st

# Custom CSS for GlowMint Elegance theme
st.markdown("""
    <style>
        /* Page background */
        .stApp {
            background-color: #FFFDF6;
        }

        /* Title and headers */
        h1, h2, h3, h4, h5 {
            color: #2C2C2C;
            font-family: 'Poppins', sans-serif;
        }

        /* Button style */
        .stButton > button {
            background-color: #FFD700;
            color: #2C2C2C;
            border-radius: 10px;
            padding: 0.5em 1em;
            font-weight: bold;
            transition: 0.3s;
        }

        .stButton > button:hover {
            background-color: #00CFC1;
            color: white;
        }

        /* Text elements */
        .stMarkdown {
            color: #2C2C2C;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Input fields */
        .stTextInput, .stSelectbox, .stTextArea {
            background-color: #AEECEF;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)
