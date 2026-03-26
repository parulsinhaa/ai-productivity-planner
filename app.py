import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Planner", page_icon="📅")

st.title("🔍 AI Model Finder + Planner")

# API Key
api_key = st.text_input("🔑 Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # ✅ MAGIC: LIST YOUR AVAILABLE MODELS
        models = genai.list_models()
        available = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
        
        st.subheader("✅ **Your Available Models:**")
        for model in available[:10]:  # Show first 10
            st.code(model)
        
        # Use first working model
        if available:
            working_model = available[0].split(':')[-1]
            model = genai.GenerativeModel(working_model)
            st.success(f"🎉 Using: **{working_model}**")
        else:
            st.error("No models available!")
            st.stop()
            
    except Exception as e:
        st.error(f"API Error: {e}")
        st.stop()
else:
    st.info("👆 Enter API key")

# Planner (only if model works)
if 'model' in locals():
    st.markdown("---")
    st.subheader("📅 Productivity Planner")
    
    query = st.text_input("Plan for:", placeholder="7-day study schedule")
    
    if st.button("✨ Generate", type="primary"):
        if query:
            with st.spinner("..."):
                try:
                    response = model.generate_content(f"Make 7-day plan for: {query}")
                    st.markdown("### 📋 **Your Plan:**")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Enter goal!")

st.caption("✅ Auto-finds your models!")
