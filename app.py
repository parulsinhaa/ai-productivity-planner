import streamlit as st
import google.generativeai as genai
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Productivity Planner",
    page_icon="📅",
    layout="centered"
)

# ---------------- STYLING ----------------
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem;
        text-align: center;
        color: #4CAF50;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: grey;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="main-title">📅 AI Productivity Planner</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Plan smarter. Stay productive. Let AI guide you.</p>', unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        st.sidebar.success("✅ Gemini Connected")
    except:
        st.sidebar.error("❌ Invalid API Key")
        st.stop()

    # ---------------- INPUT ----------------
    user_input = st.text_area(
        "✨ What do you want to plan?",
        placeholder="e.g., Plan my study schedule for exams in 5 days",
        height=120
    )

    # Example buttons
    st.markdown("### 💡 Try Examples")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📚 Study Plan"):
            user_input = "Plan my study schedule for final exams in 7 days"

    with col2:
        if st.button("💪 Workout Plan"):
            user_input = "Create a 7-day beginner workout plan"

    # ---------------- GENERATE BUTTON ----------------
    if st.button("🚀 Generate Plan", use_container_width=True):

        if user_input:
            with st.spinner("🤖 AI is generating your plan..."):

                prompt = f"""
                Create a structured, realistic, and actionable plan for: "{user_input}"

                Format strictly like:

                Day 1:
                - Task 1 (time)
                - Task 2 (time)

                Day 2:
                - Task 1 (time)
                - Task 2 (time)

                Keep it concise, practical, and include breaks where needed.
                """

                try:
                    response = model.generate_content(prompt)
                    plan = response.text

                    # Display Output
                    st.subheader("📋 Your Personalized Plan")
                    st.success("Plan generated successfully!")

                    st.markdown(plan)

                    # Copy option
                    with st.expander("📋 Copy Plan"):
                        st.code(plan)

                except Exception as e:
                    st.error(f"Error: {str(e)}")

        else:
            st.warning("⚠️ Please enter your goal first!")

else:
    st.info("""
    🔑 **Get Started:**
    
    1. Go to https://aistudio.google.com/app/apikey  
    2. Generate your FREE Gemini API Key  
    3. Paste it in the sidebar  
    4. Start planning 🚀
    """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Built with ❤️ using Streamlit + Gemini</p>",
    unsafe_allow_html=True
                )
