import streamlit as st
import google.generativeai as genai
import os

# Page config
st.set_page_config(
    page_title="AI Productivity Planner",
    page_icon="📅",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {font-size:3rem;color:#1f77b4;text-align:center;margin-bottom:2rem;font-weight:bold;}
.sub-header {font-size:1.2rem;color:#666;text-align:center;margin-bottom:2rem;}
.plan-container {background:#f8f9fa;padding:2rem;border-radius:15px;border-left:5px solid #1f77b4;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📅 AI Productivity Planner</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Get your perfect plan in seconds!</p>', unsafe_allow_html=True)

# API Key input
api_key = st.sidebar.text_input("🔑 Google Gemini API Key", type="password",
                               help="Get FREE key: aistudio.google.com/app/apikey")

if not api_key:
    st.info("""
    ## 🚀 Quick Start:
    1. Get **FREE** API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
    2. Paste in sidebar
    3. Generate your plan! ✨
    """)
    st.stop()

# Configure Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("✅ Connected!")
except:
    st.error("❌ Invalid API Key")
    st.stop()

# Main UI
col1, col2 = st.columns([3,1])

with col1:
    query = st.text_area("What to plan?", 
                        placeholder="Plan my 7-day study schedule for exams",
                        height=100)

with col2:
    st.markdown("### 💡 Examples")
    if st.button("📚 Study"): query = "7-day exam study plan"
    if st.button("💪 Workout"): query = "7-day beginner workout"
    if st.button("🏠 Weekly"): query = "weekly chores + meals"

if st.button("✨ Generate Plan", type="primary"):
    if query:
        with st.spinner("Creating your plan..."):
            prompt = f'''Create productivity plan for: "{query}"

**FORMAT EXACTLY LIKE:**
**Day 1: Title**
- Task 1 - 90min - details
- Task 2 - 30min - details

**Day 2: Title**
- etc...

Realistic times + breaks. Use • bullets only.'''
            
            response = model.generate_content(prompt)
            plan = response.text.strip()
            
            st.markdown('<div class="plan-container">', unsafe_allow_html=True)
            st.markdown("### 📋 **Your Plan**")
            st.markdown(plan)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.success("✅ Done!")
            st.balloons()

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;color:#666;'>Made with ❤️ | Gemini 1.5 Flash</p>", unsafe_allow_html=True)
