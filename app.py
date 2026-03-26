import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="AI Productivity Planner", page_icon="📅", layout="wide")

st.markdown("""
<style>
.main-header {font-size:3rem;color:#1f77b4;text-align:center;margin-bottom:2rem;font-weight:bold;}
.sub-header {font-size:1.2rem;color:#666;text-align:center;margin-bottom:2rem;}
.plan-container {background:#f8f9fa;padding:2rem;border-radius:15px;border-left:5px solid #1f77b4;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">📅 AI Productivity Planner</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Get your perfect plan instantly!</p>', unsafe_allow_html=True)

# API Key
api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password",
                               help="aistudio.google.com/app/apikey")

if not api_key:
    st.info("👆 Add your **FREE** API key in sidebar!")
    st.stop()

# Init model with safety OFF (fixes quota issues)
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        generation_config={
            "temperature": 0.7,
            "top_p": 0.8,
            "max_output_tokens": 1500,
        },
        safety_settings={
            "HARM_CATEGORY_HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_HATE_SPEECH": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_MEDIUM_AND_ABOVE",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_MEDIUM_AND_ABOVE",
        }
    )
    st.sidebar.success("✅ Ready!")
except Exception as e:
    st.error(f"❌ API Error: {str(e)[:100]}")
    st.stop()

# UI
col1, col2 = st.columns([3,1])
with col1:
    query = st.text_area("💭 What to plan?", 
                        placeholder="7-day study schedule for exams",
                        height=80,
                        help="Keep it short & specific")

with col2:
    if st.button("📚 Study Plan"): 
        query = "7-day exam study schedule"
    if st.button("💪 Fitness"): 
        query = "7-day beginner workout"
    if st.button("🏠 Weekly"): 
        query = "weekly chores schedule"

# Generate button
if st.button("✨ Create Plan", type="primary"):
    if query:
        with st.spinner("🤖 Planning..."):
            # ✅ SHORTENED PROMPT (fixes quota error)
            prompt = f"Make a 7-day plan for: {query}\n\n**Format:**\n**Day 1:**\n• Task - time\n• Task - time"
            
            try:
                response = model.generate_content(prompt)
                plan = response.text
                
                # Clean output
                st.markdown("### 📋 **Your Plan**")
                st.markdown(f"""
                <div style="background:#f8f9fa;padding:2rem;border-radius:15px;border-left:5px solid #1f77b4;">
                {plan}
                </div>
                """, unsafe_allow_html=True)
                
                st.success("✅ Plan ready!")
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Try again: {str(e)[:80]}")
                st.info("💡 Check API quota or try shorter query")
    else:
        st.warning("📝 Enter your goal!")

st.markdown("---")
st.caption("✨ Powered by Gemini 1.5 Flash")
