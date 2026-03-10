import streamlit as st
import pandas as pd
from PIL import Image
import time
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="Explore Sri Lanka AI", layout="wide")

# --- FUNCTIONS ---
def analyze_sentiment(text):
    negative_words = ['නරකයි', 'අසතුටුයි', 'කැතයි', 'එපා', 'bad', 'worst', 'poor']
    score = 0
    for word in negative_words:
        if word in text.lower():
            score -= 1
    return "Negative" if score < 0 else "Positive"

def travel_bot_response(user_query):
    query = user_query.lower()
    responses = {
        "මිල": "අපගේ පැකේජ $50 සිට ආරම්භ වේ.",
        "සීගිරිය": "සීගිරිය නැරඹීමට උදෑසන 7:00 ට පැමිණෙන්න.",
        "ආයුබෝවන්": "ආයුබෝවන්! මම ඔබේ AI සහායකයා.",
        "payment": "අපි Credit Card සහ Online Transfer භාර ගනිමු."
    }
    for key in responses:
        if key in query:
            return responses[key]
    return "කණගාටුයි, ඒ ගැන විස්තර ලබා ගැනීමට අප අමතන්න."

# --- SIDEBAR (USER PORTAL) ---
st.sidebar.title("👤 Travel Portal")
menu = st.sidebar.radio("Navigation", ["Home", "Social Feed", "AI Support", "Checkout", "Admin Panel"])

# --- HEADER ---
st.markdown("""
    <div style="background-color: #003580; padding: 15px; border-radius: 10px; text-align: center; color: white;">
        <h1>Explore Sri Lanka AI 🇱🇰</h1>
        <p>ලොව දියුණුම තාක්ෂණයෙන් යුත් සංචාරක පද්ධතිය</p>
    </div>
""", unsafe_allow_html=True)

# --- PAGES ---

if menu == "Home":
    st.header("📍 සංචාරයක් වෙන් කරවා ගන්න")
    col1, col2 = st.columns(2)
    with col1:
        dest = st.selectbox("ගමනාන්තය:", ["Sigiriya", "Ella", "Mirissa", "Kandy"])
        days = st.slider("දින ගණන:", 1, 14, 3)
    with col2:
        name = st.text_input("ඔබේ නම:")
        email = st.text_input("ඊමේල් ලිපිනය:")
    
    if st.button("Confirm Booking"):
        st.success(f"ස්තුතියි {name}! ඔබේ {dest} සංචාරය තහවුරු කරන ලදී.")
        st.balloons()

    st.markdown("---")
    st.header("📸 AI Image Identification")
    up_file = st.file_uploader("ස්ථානයක පින්තූරයක් එක් කරන්න", type=["jpg", "png"])
    if up_file:
        img = Image.open(up_file)
        st.image(img, width=400)
        st.info("AI අනාවැකිය: මෙය **සීගිරි බලකොටුව** ලෙස හඳුනා ගන්නා ලදී.")

elif menu == "Social Feed":
    st.header("📸 සංචාරක අත්දැකීම් (Social Feed)")
    with st.expander("පෝස්ටුවක් එක් කරන්න"):
        rev_text = st.text_area("ඔබේ අත්දැකීම ලියන්න:")
        if st.button("Post Now"):
            sentiment = analyze_sentiment(rev_text)
            if sentiment == "Negative":
                st.warning("ඔබේ අසතුට ගැන අප කණගාටු වෙමු. සහාය කණ්ඩායම දැන්ම ක්‍රියාත්මක වේ.")
                st.session_state['alert'] = f"අසතුටු පාරිභෝගිකයෙක්: {rev_text}"
            else:
                st.success("පෝස්ටුව සාර්ථකව පළ කරන ලදී!")

elif menu == "AI Support":
    st.header("🤖 AI Virtual Assistant")
    msg = st.chat_input("මගෙන් ඕනෑම දෙයක් අසන්න...")
    if msg:
        st.write(f"👤 ඔබ: {msg}")
        st.write(f"🤖 Bot: {travel_bot_response(msg)}")

elif menu == "Checkout":
    st.header("💳 Secure Payment Gate")
    st.write("මුළු එකතුව: **$100.00**")
    st.text_input("කාඩ්පත් අංකය")
    if st.button("දැන්ම ගෙවන්න (Pay Now)"):
        with st.spinner("Processing..."):
            time.sleep(2)
            st.success("ගෙවීම සාර්ථකයි! ඉන්වොයිසිය ඊමේල් කරන ලදී.")

elif menu == "Admin Panel":
    st.header("🛡️ Admin Dashboard")
    if 'alert' in st.session_state:
        st.error(f"⚠️ හදිසි අවධානයට: {st.session_state['alert']}")
    else:
        st.info("පද්ධතියේ දෝෂ කිසිවක් නැත. සියලු දෙනා සතුටින්! ✅")
