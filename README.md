
# Gemini Talk Streaming API

This is a FastAPI project that uses [LangChain](https://github.com/langchain-ai/langchain) to stream responses from the Google Gemini language model via a simple API endpoint. The model used is `gemini-2.0-flash`, and streaming is enabled for real-time response delivery.

---

## 🚀 Features

- FastAPI-based HTTP server
- Integration with Google's Gemini model via LangChain
- Streaming responses using `StreamingResponse`
- Environment-based API key loading
- Fully async handling

---

## 📦 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- LangChain
- `langchain-google-genai`
- `python-dotenv`

---

## 📁 Project Structure

.
├── main.py # FastAPI application
├── .env # Environment variables (not committed)
├── .gitignore
└── README.md



---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alihaider22/gemini-talk-fastapi-backend.git
   cd gemini-talk-fastapi-backend

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Create a `.env` file and set your API key**
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here

5. **Start the FastAPI server using Uvicorn**
   ```bash
   uvicorn main:app --reload

---

### 📄 **License**

This project is licensed under the MIT License.
