import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Perplexity client
client = OpenAI(
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
)

st.title("Question Answering with Streamlit (Perplexity)")

# Get user question - pressing Enter will submit
question = st.text_input("Ask a question (press Enter to submit):")

if question:
    st.write("Thinking...")
    try:
        # Get completion from Perplexity
        completion = client.chat.completions.create(
            model=os.getenv("PERPLEXITY_MODEL_NAME"),
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
        )

        # Display the answer
        if completion.choices:
            st.write("Answer:")
            st.write(completion.choices[0].message.content)
        else:
            st.write("No answer received from the model.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
