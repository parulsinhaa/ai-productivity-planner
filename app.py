import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="AI Productivity Planner", page_icon="📅")

# Title
st.title("📅 AI Productivity Planner")
st.write("Tell me your goal and I'll create a structured plan for you!")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    # User input
    user_input = st.text_area("What do you want to plan?")

    if st.button("Generate Plan"):
        if user_input:
            with st.spinner("Generating your plan..."):
                
                prompt = f"""
                Create a structured and practical plan for: {user_input}

                Format:
                Day 1:
                - Task 1
                - Task 2

                Day 2:
                - Task 1
                - Task 2

                Keep it realistic, concise, and actionable.
                """

                response = model.generate_content(prompt)
                
                st.subheader("📋 Your Plan")
                st.write(response.text)

        else:
            st.warning("Please enter something!")
else:
    st.info("Enter your Gemini API key in sidebar to start.")
