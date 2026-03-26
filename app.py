import streamlit as st
import google.generativeai as genai

# Config
st.set_page_config(page_title="AI Planner", page_icon="📅", layout="centered")

st.title("🤖 AI Productivity Planner")
st.markdown("*Free AI plans for study, work, fitness & more*")

# API Key
api_key = st.text_input("🔑 Google Gemini API Key:", type="password")

if not api_key:
    st.info("""
    **Get FREE API Key:**
    1. [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
    2. Copy key → paste here
    3. Click Generate! ✨
    """)
    st.stop()

# ✅ TESTED WORKING MODELS ONLY
models = ["gemini-pro", "gemini-1.5-flash-latest", "gemini-pro-vision"]

model = None
for m in models:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(m)
        st.success(f"✅ Using: **{m}**")
        break
    except:
        continue

if not model:
    st.error("❌ No working model found. Check API key!")
    st.stop()

# Simple input
query = st.text_input("💡 What do you want to plan?", 
                     placeholder="7-day study schedule for exams")

# Quick buttons
col1, col2, col3 = st.columns(3)
if col1.button("📚 Study"): query = "7 day study plan for exams"
if col2.button("🏋️ Fitness"): query = "7 day workout plan"
if col3.button("📋 Weekly"): query = "weekly productivity plan"

# Generate!
if st.button("✨ Make My Plan", type="primary"):
    if query:
        with st.spinner('Planning...'):
            # ULTRA-SIMPLE PROMPT
            prompt = f"7 day plan for: {query}. Use format: **Day 1:** bullet points"
            
            try:
                response = model.generate_content(prompt)
                st.subheader("📋 Your Plan:")
                st.markdown(response.text)
                st.success("✅ Done!")
            except Exception as e:
                st.error(f"⚠️ {str(e)}")
                st.info("Try shorter query or new API key")
    else:
        st.warning("👆 Enter your goal first!")

st.markdown("---")
st.caption("✅ Powered by Google Gemini")
