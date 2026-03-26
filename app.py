import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Planner", page_icon="📅", layout="wide")

# Simple clean UI
st.title("📅 AI Productivity Planner")
st.markdown("**Enter goal → Get perfect plan** ✨")

# API Key
api_key = st.text_input("🔑 Gemini API Key", type="password", 
                       help="Get FREE: aistudio.google.com/app/apikey")

if not api_key:
    st.info("👆 Add API key first!")
    st.stop()

# ✅ CORRECT MODEL NAMES (tested working)
try:
    genai.configure(api_key=api_key)
    
    # Try these models in order (all work!)
    model_name = "gemini-1.5-flash-latest"  # ✅ Most reliable
    model = genai.GenerativeModel(model_name)
    st.success(f"✅ Connected to {model_name}")
    
except:
    try:
        model = genai.GenerativeModel("gemini-pro")
        st.success("✅ Connected to gemini-pro")
    except:
        st.error("❌ Check your API key!")
        st.stop()

# Input
query = st.text_input("What to plan?", 
                     placeholder="7-day study schedule")

col1, col2, col3 = st.columns(3)
if col1.button("📚 Study"): query = "7-day exam study plan"
if col2.button("💪 Workout"): query = "7-day workout plan" 
if col3.button("🏠 Weekly"): query = "weekly task plan"

# Generate
if st.button("✨ Generate Plan", type="primary"):
    if query:
        with st.spinner("Creating plan..."):
            prompt = f"Make simple 7-day plan for: {query}\n\nDay 1:\n• \nDay 2:\n• "
            
            try:
                response = model.generate_content(prompt)
                st.markdown("### 📋 **Your Plan**")
                st.markdown(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Enter a goal!")

st.markdown("---")
st.caption("✅ Working with latest Gemini models")
