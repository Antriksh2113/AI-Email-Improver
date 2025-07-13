# AI-Email-Improver

Instantly rewrite your email drafts in various tones using open-source LLMs. Built with FastAPI, Streamlit, and Hugging Face APIs.

## 🚀 Overview
AI Email Improver is a simple web application that helps users rewrite their email drafts in different tones—such as polite, formal, friendly, concise, and persuasive. It uses Hugging Face's open-source Mistral model (via the featherless router) to improve or reframe emails while keeping your text private and local to the extent possible.

The backend is powered by FastAPI, while the frontend is built using Streamlit for an interactive user experience.

## 🌐 Live Demo
Currently runs locally. After setup, access:

Frontend (Streamlit): http://localhost:8501

Backend (FastAPI): http://localhost:8000/rewrite

## 🔧 Features
* ✅ Rewrite any email in 5 tones: Formal, Polite, Friendly, Concise, Persuasive.
* ✅ Hugging Face LLM (Mistral) integration via Featherless API.
* ✅ Clean and intuitive UI with Streamlit.
* ✅ Configurable via .env file.
* ✅ Modular codebase (easy to expand or integrate).

## 🛠️ Setup Instructions

1. Clone the Repository

2. Create a Virtual Environment
  * python -m venv venv
  * source venv/bin/activate     # For macOS/Linux
  * venv\Scripts\activate.bat    # For Windows

3. Install Requirements
   * pip install -r requirements.txt

4. Add Hugging Face API Key
  * Create a .env file in the root directory:
  * HF_TOKEN=your_huggingface_api_key_here
  * You can get your token from: https://huggingface.co/settings/tokens

5. Run the Backend
* cd backend
* uvicorn app:app --reload
* This will start the FastAPI server with CORS enabled.

6. Run the Frontend
* cd frontend
* streamlit run app.py
* Streamlit UI will open in your browser at: http://localhost:8501

## 🧠 How It Works
- Under the hood:
  - llm.py: Encapsulates API call logic using requests to Hugging Face
  - EmailRewriter: Builds the prompt → sends it → parses and returns result
  - Streamlit frontend talks to backend using requests.post() to trigger rewriting

## 🙌 Acknowledgements
  * Hugging Face
  * MistralAI
  * FastAPI
  * Streamlit

