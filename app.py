import streamlit as st
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Productivity Planner",
    page_icon="📅",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("📅 AI Productivity Planner")
st.write("Plan smarter. Stay productive. Let AI guide you.")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔑 Enter Gemini API Key")
api_key = st.sidebar.text_input("API Key", type="password")

if api_key:
    try:
        # Configure API
        genai.configure(api_key=api_key)

        # ✅ WORKING MODEL NAME
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        st.sidebar.success("✅ Connected successfully!")

        # ---------------- INPUT ----------------
        user_input = st.text_area(
            "✨ What do you want to plan?",
            placeholder="e.g., Plan my study schedule for exams in 5 days",
            height=120
        )

        # ---------------- BUTTON ----------------
        if st.button("🚀 Generate Plan", use_container_width=True):

            if user_input:
                with st.spinner("🤖 Generating your plan..."):

                    prompt = f"""
                    Create a structured, realistic and practical plan for: "{user_input}"

                    Format strictly like:

                    Day 1:
                    - Task 1 (time)
                    - Task 2 (time)

                    Day 2:
                    - Task 1 (time)
                    - Task 2 (time)

                    Keep it simple, actionable, and time-bound.
                    """

                    try:
                        response = model.generate_content(prompt)
                        st.subheader("📋 Your Plan")
                        st.success("✅ Plan generated successfully!")
                        st.write(response.text)

                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

            else:
                st.warning("⚠️ Please enter your goal first!")

    except Exception as e:
        st.sidebar.error(f"❌ Invalid API Key: {str(e)}")

else:
    st.info("""
    🔑 **Get your FREE Gemini API key:**
    
    👉 https://aistudio.google.com/app/apikey
    
    Paste it in the sidebar and start 🚀
    """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Built with ❤️ using Streamlit + Gemini</p>",
    unsafe_allow_html=True
                    )
