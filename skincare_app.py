import streamlit as st

# ✅ PAGE SETUP (must be the first Streamlit command)
st.set_page_config(page_title="GeneGlow Skincare", layout="centered")

# ✅ Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "welcome"  # Default page

# ✅ CUSTOM CSS (to make the app look clean & modern)
st.markdown("""
    <style>
        .stApp {background-color: #FFFDF6; font-family: 'Segoe UI', sans-serif;}
        .title {text-align: center; font-size: 48px; font-weight: bold; color: #2C2C2C;}
        .subtitle {text-align: center; font-size: 20px; color: #00CFC1; margin-bottom: 30px;}
        .stButton > button {background-color: #FFD700; color: #2C2C2C; border-radius: 30px; padding: 0.5em 2em;}
        .stButton > button:hover {background-color: #00CFC1; color: white;}
    </style>
""", unsafe_allow_html=True)

# ✅ Page Navigation Logic
def switch_page(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

# --- WELCOME PAGE ---
if st.session_state.page == "welcome":
    st.markdown('<div class="title">Welcome to GeneGlow Skincare</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your Personalized Skincare Journey Starts Here!</div>', unsafe_allow_html=True)

    st.markdown("""
        GeneGlow provides tailored skincare solutions based on **science and natural remedies**.
        We help you identify your **skin type**, provide **anti-aging tips**, and suggest **products available in your country**.

        🔥 **Discover your perfect skincare routine now!**
    """)

    if st.button("🚀 Get Started"):
        switch_page("login")

# --- LOGIN PAGE ---
elif st.session_state.page == "login":
    st.markdown('<div class="title">GeneGlow Login</div>', unsafe_allow_html=True)

    email = st.text_input("📧 Email Address")
    password = st.text_input("🔒 Password", type="password")

    if st.button("Login"):
        if email == "test@example.com" and password == "password":  # Replace with real authentication
            switch_page("quiz")
        else:
            st.error("Invalid credentials. Please try again.")

    if st.button("🔑 Don't have an account? Sign up"):
        switch_page("signup")

# --- QUIZ PAGE ---
elif st.session_state.page == "quiz":
    st.title("🌸 GeneGlow Skin Quiz")
    st.subheader("Discover your skin type and learn how to reverse aging naturally.")

    age = st.slider("How old are you?", 12, 80, 20)
    skin_type = st.selectbox("What best describes your skin?", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])
    concern = st.text_area("What is your biggest skin concern? (e.g., fine lines, acne, wrinkles, etc.)")
    country = st.selectbox("🌍 Which country are you from?", ["USA", "UK", "India", "Pakistan", "Australia", "Canada", "Other"])

    if st.button("🔍 Get My Skin Report"):
        st.success("Thank you for completing the quiz! Here's your personalized skincare guide:")

        if skin_type == "Oily":
            st.markdown("- 🧼 **Use a foaming cleanser** with salicylic acid to clear pores.")
            st.markdown("- 🍋 **Incorporate Vitamin C** for brighter skin and anti-aging.")
            st.markdown("**💡 Home Remedy**: Apply aloe vera gel or green tea as a face mask for oil control.")
        elif skin_type == "Dry":
            st.markdown("- 💦 **Hydrate with a rich moisturizer** and use hyaluronic acid.")
            st.markdown("- 🚿 **Avoid hot showers** as they dry out your skin.")
            st.markdown("**💡 Home Remedy**: Try a honey and olive oil mask to hydrate dry skin.")
        elif skin_type == "Combination":
            st.markdown("- 🌿 **Use different products** for T-zone vs cheeks.")
            st.markdown("**💡 Home Remedy**: A cucumber mask can soothe both dry and oily skin.")
        elif skin_type == "Sensitive":
            st.markdown("- 🚫 **Use fragrance-free and gentle products**.")
            st.markdown("**💡 Home Remedy**: Chamomile tea bags help calm irritated skin.")

        # 🧑‍⚕️ Reverse Aging Tips
        st.markdown("### 🧑‍⚕️ Reverse Aging Tips:")
        st.markdown("- 🛡️ **Apply sunscreen daily** (even indoors) to prevent premature aging.")
        st.markdown("- 🌙 **Use retinol at night** for smoother skin.")
        st.markdown("- 💧 **Stay hydrated** and eat foods rich in antioxidants.")

        # 🌍 Country-Specific Product Recommendations
        st.markdown("### 🌍 Recommended Products in Your Country:")
        if country == "USA":
            st.markdown("- 🧴 Neutrogena Oil-Free Acne Wash")
            st.markdown("- 🌟 Olay Regenerist Micro-Sculpting Cream (Anti-aging)")
        elif country == "UK":
            st.markdown("- 🌿 The Ordinary Niacinamide 10% + Zinc 1%")
            st.markdown("- 🔥 Eucerin Q10 Anti-Wrinkle Face Cream")
        elif country == "India":
            st.markdown("- 🌱 Himalaya Herbals Purifying Neem Face Wash")
            st.markdown("- 🌾 Biotique Bio Wheat Germ Anti-Aging Cream")
        elif country == "Pakistan":
            st.markdown("- 🌙 Nivea Men Dark Spot Reduction Face Wash")
            st.markdown("- 🌟 POND’S Age Miracle Wrinkle Corrector Night Cream")
        elif country == "Australia":
            st.markdown("- 🍃 Sukin Foaming Facial Cleanser")
            st.markdown("- 🧪 Aesop Parsley Seed Anti-Oxidant Serum")
        elif country == "Canada":
            st.markdown("- 💦 Neutrogena Hydro Boost Water Gel")
            st.markdown("- 🌙 Kiehl’s Midnight Recovery Concentrate")
        else:
            st.markdown("- 🌍 Research local skincare brands for the best products in your country.")

    if st.button("🔙 Back to Home"):
        switch_page("welcome")
