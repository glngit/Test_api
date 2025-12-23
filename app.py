import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI client
# The API key is loaded automatically from the OPENAI_API_KEY environment variable
# or can be set explicitly. The user should have a .env file with the key.
# Example .env file:
# OPENAI_API_KEY="hf_..." or HF_TOKEN="hf_..."
# I will use the base_url from the previous version of the file.
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"), # Or another env var the user has set
)

st.title("Question Answering with Streamlit")

# Get user question
question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if question:
        st.write("Thinking...")
        try:
            # Get completion from the model
            completion = client.chat.completions.create(
                model="zai-org/GLM-4.7:zai-org",
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
    else:
        st.warning("Please enter a question.")
