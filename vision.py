# Q&A Chatbot
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get respones
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our Streamlit app
st.set_page_config(
    page_title="Gemini Mode Sappy Image Recognition",
    page_icon=":camera:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS styling
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Add a header with custom styles
st.markdown(
    "<div style='text-align: center; background-color: #4c9dff; padding: 20px; border-radius: 10px;'><h1 style='color: white; margin: 0;'>Sap's Image Application</h1></div>",
    unsafe_allow_html=True
)

# Create columns for input and image
col1, col2 = st.columns([2, 1])

# Input column
with col1:
    st.subheader("Input Prompt")
    input = st.text_area("Enter your prompt here:", height=200, placeholder="Type your prompt...")

# Image column
with col2:
    st.subheader("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button
submit = st.button("Tell me about the image", use_container_width=True)

# If submit button is clicked
if submit:
    if image is None:
        st.warning("Please upload an image first.", icon="⚠️")
    else:
        with st.spinner("Generating response..."):
            response = get_gemini_response(input, image)
        st.success("Response generated!", icon="✅")
        st.write(response)
