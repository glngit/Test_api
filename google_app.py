import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("Question Answering with Streamlit (Gemini)")

# Get user question - pressing Enter will submit
question = st.text_input("Ask a question (press Enter to submit):")

if question:
    st.write("Thinking...")
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel(os.getenv("GEMINI_MODEL_NAME"))
        
        # Generate response
        response = model.generate_content(question)
        
        # Display the answer
        if response.text:
            st.write("Answer:")
            st.write(response.text)
        else:
            st.write("No answer received from the model.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")
