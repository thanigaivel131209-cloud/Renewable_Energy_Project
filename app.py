import streamlit as st

st.set_page_config(
    page_title="Renewable Energy Output Predictor",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Renewable Energy Output Predictor")

st.subheader("SDG 7 - Affordable and Clean Energy")

st.write("""
Welcome to the Renewable Energy Output Predictor.

Use the sidebar to navigate through:
- Home
- Solar Prediction
- Wind Prediction
- Analytics Dashboard
- AI Chatbot
""")

st.success("Project Loaded Successfully!")