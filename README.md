# Streamlit Q&A App with Gemini API - Setup Guide

This guide walks you through setting up the Streamlit Question Answering application with Google Gemini API on a virtual machine.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (optional but recommended)

## Setup Instructions

### 1. Clone or Download the Project

Navigate to your project directory:

```bash
cd /path/to/RAG/Test_api
```

### 2. Create and Activate Virtual Environment (Recommended)

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install:
- **streamlit** - Web app framework
- **openai** - OpenAI API client (for future use)
- **python-dotenv** - Environment variable management
- **google-generativeai** - Google Gemini API client

### 4. Configure Environment Variables

Create or update the `.env` file in the project directory with your API keys:

```env
# HuggingFace API Token (if using HuggingFace models)
HF_TOKEN="your-huggingface-token-here"

# Google Gemini API Key (Required for this app)
GEMINI_API_KEY="your-gemini-api-key-here"

# Model name (for HuggingFace/Groq)
MODEL_NAME="openai/gpt-oss-20b:groq"
```

#### How to Get Your Gemini API Key:

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Click on **"Get API Key"** or **"Create new API key"**
3. Select or create a Google Cloud project
4. Copy the generated API key
5. Paste it into the `.env` file as `GEMINI_API_KEY`

**Important:** Never commit your `.env` file to version control. It contains sensitive credentials.

### 5. Run the Application

There are two app versions available:

#### Option A: Use Gemini API (Recommended)

```bash
streamlit run google_app.py
```

This uses Google's Gemini model for responses.

#### Option B: Use Original App

```bash
streamlit run app.py
```

This uses the configured model from `MODEL_NAME` in `.env`.

### 6. Access the Web Interface

Once running, Streamlit will display:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://your-vm-ip:8501
```

Open the URL in your browser and start asking questions!

## Files Overview

- **google_app.py** - Main app using Gemini API
- **app.py** - Alternative app using HuggingFace/Groq
- **.env** - Environment variables (API keys) - **DO NOT COMMIT**
- **requirements.txt** - Python dependencies
- **README.md** - This file

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "GEMINI_API_KEY not found"

**Solution:** Make sure:
1. `.env` file exists in the project directory
2. `GEMINI_API_KEY="your-key"` is set in `.env`
3. Run `pip install python-dotenv` if not installed

### Issue: "Error 402: You have reached the free monthly usage limit"

**Solution:** This happens with Groq/HuggingFace models. Switch to Gemini:
```bash
streamlit run google_app.py
```

### Issue: Virtual Environment Not Activated

**Solution:** Reactivate your virtual environment:

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

## Environment Variables Reference

| Variable | Required | Source | Example |
|----------|----------|--------|---------|
| `GEMINI_API_KEY` | Yes | Google AI Studio | `AIza...` |
| `HF_TOKEN` | No | HuggingFace Settings | `hf_...` |
| `MODEL_NAME` | No | Manual config | `openai/gpt-oss-20b:groq` |

## Performance Tips for VM

- **Low Memory:** If your VM has limited resources, Streamlit may be slow. Consider:
  - Running on a VM with at least 2GB RAM
  - Using a simpler model
  - Clearing cache: `streamlit cache clear`

- **Remote Access:** To access from another machine:
  ```bash
  streamlit run google_app.py --server.address 0.0.0.0
  ```

## Next Steps

1. Test the app with a simple question
2. Customize the UI in `google_app.py` as needed
3. Integrate with your RAG pipeline
4. Deploy to production when ready

## Support

For issues with:
- **Gemini API:** [Google AI Documentation](https://ai.google.dev/docs)
- **Streamlit:** [Streamlit Docs](https://docs.streamlit.io)
- **Python:** [Python Official Docs](https://docs.python.org)
