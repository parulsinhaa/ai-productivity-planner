import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="AI Productivity Planner", page_icon="📅")

st.title("📅 AI Productivity Planner")

# Sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)

        # ✅ MOST STABLE MODEL (WORKS NOW)
        model = genai.GenerativeModel("gemini-1.5-pro-latest")

        st.sidebar.success("Connected ✅")

        user_input = st.text_area("What do you want to plan?")

        if st.button("Generate Plan"):
            if user_input:
                with st.spinner("Generating..."):

                    prompt = f"""
                    Create a simple structured plan for: {user_input}

                    Format:
                    Day 1:
                    - Task 1
                    - Task 2

                    Day 2:
                    - Task 1
                    - Task 2
                    """

                    response = model.generate_content(prompt)

                    st.subheader("Your Plan")
                    st.write(response.text)

            else:
                st.warning("Enter something!")

    except Exception as e:
        st.error(f"Error: {str(e)}")

else:
    st.info("Enter API key to start")

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit + Gemini")
